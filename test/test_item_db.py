from unittest import TestCase, mock

from botocore.exceptions import ClientError

from demo.datasource.item_db import Item, ItemDB
from demo.datasource.dynamo_db import local_dynamo_client, local_dynamo_resource


def delete_local_table(client, table_name):
    """Delete local Dynamodb table.

    :param client: Botot3 DynamoDB client
    :type client: boto3.client
    :param table_name: Name of table to delete
    :type table_name: str
    :return:
    """
    assert client._endpoint.host == 'http://127.0.0.1:8000', "Can only delete local endpoint," \
                                                             " not {}".format(client._endpoint.host)
    response = client.delete_table(
        TableName=table_name
    )
    print("Deleting local table '{}': {}".format(table_name, response))


def create_test_table(resource):
    """Create 'test' table locally.

    :param resource: Resource to build table against
    :param resource: boto3.resource
    :return: Pointer to local table
    """
    response = resource.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'item_id',
                'AttributeType': 'S'
            }
        ],
        TableName='test-items',
        KeySchema=[
            {
                'AttributeName': 'item_id',
                'KeyType': 'HASH'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        },
        StreamSpecification={
            'StreamEnabled': False,
        }
    )
    print("Creating local table 'test-items': {}".format(response))
    return resource.Table('test-items')


class TestItemDB(TestCase):
    scenario_id = str(777)
    rule_config = {
        "item_id": '777',
        "value": "test"
    }
    test_item = Item(**rule_config)
    test_item_id = test_item.item_id

    @mock.patch('demo.datasource.item_db.dynamodb', local_dynamo_resource)
    def setUp(self):
        try:
            self.table = create_test_table(local_dynamo_resource)
            self.item_db = ItemDB()
        except ClientError as e:
            print(e.response['Error']['Code'])
            delete_local_table(local_dynamo_client, 'test-items')

    def tearDown(self):
        delete_local_table(local_dynamo_client, 'test-items')

    def test_upload_rule(self):
        """Test that a rule is uploaded correctly."""
        self.item_db.upload_item(self.test_item)
        response = local_dynamo_client.describe_table(TableName='test-items')
        self.assertEqual(response['Table']['ItemCount'], 1)
