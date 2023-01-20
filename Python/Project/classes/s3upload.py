import logging
import boto3
from botocore.exceptions import ClientError
import os

file = "contactbook.csv"


def upload_file(bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
