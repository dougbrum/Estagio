from botocore.exceptions import ClientError
import logging
import boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id = input('Digite seu key id: '),
    aws_secret_access_key = input('Digite a secret key: ')
    )

def create_bucket(bucketNome):
    try:
        s3_client.create_bucket(Bucket=bucketNome)
    except ClientError(e) as e:
        logging.error(e)
        return False
    return True

create_bucket(sprint7dougbrum)