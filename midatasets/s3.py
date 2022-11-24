import logging
import boto3
from botocore.exceptions import ClientError
import os


def check_exists_s3(bucket: str, prefix: str):
    s3 = boto3.client("s3")
    try:
        s3.head_object(Bucket=bucket, Key=prefix)
        return True
    except ClientError:
        return False


def upload_file(file_name, bucket, prefix=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param prefix: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 prefix was not specified, use file_name
    if prefix is None:
        prefix = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client("s3")
    try:
        response = s3_client.upload_file(file_name, bucket, prefix)
    except ClientError as e:
        logging.error(e)
        return False
    return True