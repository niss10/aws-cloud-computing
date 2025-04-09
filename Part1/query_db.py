from boto3.dynamodb.conditions import Attr
import boto3
import time
from datetime import datetime, timedelta

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# Get the table
table = dynamodb.Table('UserLogins')

# Current and cutoff timestamps
now = int(time.time())
seven_days_ago = now - (7 * 24 * 60 * 60)

# Scan the table with a filter
response = table.scan(
    FilterExpression=Attr('Timestamp').gte(seven_days_ago)
)

# Extract and print users
print("Users logged in within the last 7 days:")
for item in response['Items']:
    print(item)
