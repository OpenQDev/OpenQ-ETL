import extract
import transform
import load
import extract
import datetime
import os
import boto3
from dotenv import dotenv_values

def main():
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
    start_date = datetime.datetime(2015, 1, 1, 14)
    end_date = start_date + datetime.timedelta(hours=2)
    
    while start_date <= end_date:
        start_date += datetime.timedelta(hours=1)
        date_str = start_date.strftime("%Y-%m-%d-%H")
        # Check if there is already an S3 object
        s3_object_key = f"insights.github_events.{date_str.replace('-', '')}.csv"
        response = s3.list_objects_v2(Bucket='githubarchive', Prefix=s3_object_key)
        if 'Contents' in response:
            print(date_str, "	already exists in S3, skipping...")
            continue
        else:
          print(date_str, "	downloading...")
          archive_exists = extract.extract_data(date_str)
          if archive_exists:
            print(date_str, "	downloaded!")
            print(date_str, "	transforming to CSV...")
            transform.jsonl_to_csv(date_str)
            print(date_str, "	transformed!")
            print(date_str, "	uploading to S3...")
            load.upload_to_s3(f"./csv/insights.github_events.{date_str.replace('-', '')}.csv")
            print(date_str, "	uploaded to S3!")
          else:
              print(date_str, "	is not yet in Github Archive. Exiting...")
              return

if __name__ == "__main__":
    main()
