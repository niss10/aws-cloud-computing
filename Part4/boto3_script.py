import boto3

# ----- CONFIG -----
bucket_name = 'nisarg-hw3-stack-bucket-dev'
dynamodb_table_name = 'StudentTasks'
region = 'us-east-1'

# 1. List all files in a specified S3 bucket
def list_s3_objects():
    s3 = boto3.client('s3')
    print(f"\n Listing objects in bucket: {bucket_name}")
    response = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f" - {obj['Key']} ({obj['Size']} bytes)")
    else:
        print("Bucket is empty or does not exist.")

# 2. Create a DynamoDB table
def create_dynamodb_table():
    dynamodb = boto3.client('dynamodb', region_name=region)
    existing_tables = dynamodb.list_tables()['TableNames']
    if dynamodb_table_name in existing_tables:
        print(f"\n Table '{dynamodb_table_name}' already exists.")
        return

    print(f"\n Creating DynamoDB table: {dynamodb_table_name}")
    dynamodb.create_table(
        TableName=dynamodb_table_name,
        KeySchema=[
            {'AttributeName': 'id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    print(" Waiting for table to be active...")
    waiter = boto3.client('dynamodb').get_waiter('table_exists')
    waiter.wait(TableName=dynamodb_table_name)
    print(" Table is now active.")

# 3. Insert an item into the DynamoDB table
def insert_item():
    dynamodb = boto3.resource('dynamodb', region_name=region)
    table = dynamodb.Table(dynamodb_table_name)

    item = {
        'id': 'task-001',
        'task_name': 'Boto3 Script Task',
        'status': 'completed'
    }

    print(f"\n Inserting item into table '{dynamodb_table_name}': {item}")
    table.put_item(Item=item)
    print(" Item inserted successfully.")

# ----- RUN THE TASKS -----
if __name__ == '__main__':
    list_s3_objects()
    create_dynamodb_table()
    insert_item()
