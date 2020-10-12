from os import environ as env

import boto3

try:
    from local_secure import AWS_ACCESS_ID, AWS_SECRET_KEY
except ImportError:
    try:
        AWS_ACCESS_ID = env['AWS_ACCESS_ID']
        AWS_SECRET_KEY = env['AWS_SECRET_KEY']
    except KeyError:
        AWS_SECRET_KEY = None
        AWS_ACCESS_ID = None

if AWS_ACCESS_ID is not None and AWS_SECRET_KEY is not None:
    dynamodb = boto3.resource('dynamodb',
                              aws_access_key_id=AWS_ACCESS_ID,
                              aws_secret_access_key=AWS_SECRET_KEY,
                              region_name='eu-west-1')
else:
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')


try:
    from severn.local_secure import AWS_ACCESS_ID, AWS_SECRET_KEY
except ImportError:
    try:
        AWS_ACCESS_ID = env['AWS_ACCESS_ID']
        AWS_SECRET_KEY = env['AWS_SECRET_KEY']
    except KeyError:
        AWS_SECRET_KEY = None
        AWS_ACCESS_ID = None

if AWS_ACCESS_ID is not None and AWS_SECRET_KEY is not None:
    local_dynamo_resource = boto3.resource('dynamodb',
                                           aws_access_key_id=AWS_ACCESS_ID,
                                           aws_secret_access_key=AWS_SECRET_KEY,
                                           region_name='eu-west-1',
                                           endpoint_url='http://127.0.0.1:8000')
    local_dynamo_client = boto3.client('dynamodb',
                                       aws_access_key_id=AWS_ACCESS_ID,
                                       aws_secret_access_key=AWS_SECRET_KEY,
                                       region_name='eu-west-1',
                                       endpoint_url='http://127.0.0.1:8000')
else:
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')
    local_dynamo_resource = boto3.resource('dynamodb', region_name='eu-west-1', endpoint_url='http://127.0.0.1:8000')
    local_dynamo_client = boto3.client('dynamodb', region_name='eu-west-1', endpoint_url='http://127.0.0.1:8000')
