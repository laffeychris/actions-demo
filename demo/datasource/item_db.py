from decimal import Decimal

from demo.datasource.dynamo_db import dynamodb


def dict_to_dynamo_item(d):
    if not isinstance(d, dict):
        if isinstance(d, float):
            # Dynamodb does not accept float
            return Decimal(str(d))
        elif isinstance(d, list):
            return [dict_to_dynamo_item(i) for i in d]
        else:
            return d
    else:
        item = {}
        for k, v in d.items():
            if v is not None:
                item[k] = dict_to_dynamo_item(v)
        return item


class Item:
    def __init__(self, item_id, value):
        self.item_id = item_id
        self.value = value

    def to_dynamo_item(self):
        """Format the Message for upload to DynamoDB."""
        item = dict_to_dynamo_item(self.__dict__)
        return item


class ItemDB:

    def __init__(self):
        self.table = dynamodb.Table('test-items')

    def upload_item(self, item: Item):
        """Upload record to DynamoDB."""
        paras = {
            "Item": item.to_dynamo_item(),
            "ConditionExpression": "attribute_not_exists(item_id)"
        }
        print("Uploading item: {}".format(item.item_id))
        return {
            'upload_to_severn-rules': self.table.put_item(**paras)
        }
