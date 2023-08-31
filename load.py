import boto3
from dotenv import dotenv_values

def upload_to_s3(file_name):
    # Load the environment variables from the .env file
    env_vars = dotenv_values()

    # Get the AWS access key and secret access key from the environment variables
    access_key = env_vars['AWS_ACCESS_KEY_ID']
    secret_key = env_vars['AWS_SECRET_ACCESS_KEY']

    # Create a boto3 session with the access keys
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    # Use the session to create an S3 client
    s3 = session.client('s3')

    # Upload the file to the root of the "githubarchive" bucket
    s3.upload_file(file_name, 'githubarchive', file_name.split('/')[-1])
