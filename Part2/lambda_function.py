import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        size = record['s3']['object']['size']
        logger.info(f"New file uploaded to {bucket}: {key} ({size} bytes)")
    return {
        'statusCode': 200,
        'body': json.dumps('File info logged to CloudWatch')
    }
