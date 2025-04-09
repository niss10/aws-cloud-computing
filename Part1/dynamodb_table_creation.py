import boto3

# Initialize the DynamoDB resource
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # change region if needed

# Create the table
table = dynamodb.create_table(
    TableName='UserLogins',
    KeySchema=[
        {'AttributeName': 'UserID', 'KeyType': 'HASH'},      # Partition key
        {'AttributeName': 'Timestamp', 'KeyType': 'RANGE'}   # Sort key
    ],
    AttributeDefinitions=[
        {'AttributeName': 'UserID', 'AttributeType': 'S'},
        {'AttributeName': 'Timestamp', 'AttributeType': 'N'}
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists
table.meta.client.get_waiter('table_exists').wait(TableName='UserLogins')

print("Table created successfully!")
