import time
from datetime import datetime, timedelta

import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # change region if needed

# Get the table
table = dynamodb.Table('UserLogins')

# Generate timestamps
now = int(time.time())
seven_days_ago = now - (7 * 24 * 60 * 60)

# Sample data
users = [
    {
        'UserID': 'user1',
        'Timestamp': now,
        'Name': 'Nisarg Patel',
        'Email': 'nisarg@example.com',
        'LastLogin': datetime.utcfromtimestamp(now).isoformat()
    },
    {
        'UserID': 'user2',
        'Timestamp': seven_days_ago,
        'Name': 'Parth Patel',
        'Email': 'parth@example.com',
        'LastLogin': datetime.utcfromtimestamp(seven_days_ago).isoformat()
    },
    {
        'UserID': 'user3',
        'Timestamp': now - 10 * 24 * 60 * 60,
        'Name': 'Magan Patel',
        'Email': 'magan@example.com',
        'LastLogin': datetime.utcfromtimestamp(now - 10 * 24 * 60 * 60).isoformat()
    }
]

# Insert the data
for user in users:
    table.put_item(Item=user)

print("Sample data inserted.")
