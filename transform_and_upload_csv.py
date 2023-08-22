from dotenv import load_dotenv
import os
import csv
import jsonlines

load_dotenv()

# Read environment variables
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
port = os.environ['PORT']
filepath = os.environ['FILEPATH']
s3_bucket = os.environ['S3_BUCKET_NAME']
s3_prefix = os.environ['S3_PREFIX']

# Load data from JSONL file using jsonlines
github_data = []
with jsonlines.open(filepath) as reader:
    for event in reader:
        github_data.append(event)

# Create a CSV file
csv_filename = 'github_events.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'event_type', 'actor_id', 'actor_login', 'repo_id', 'repo_name', 'repo_url', 'created_at']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for event in github_data:
        writer.writerow({
            'id': int(event["id"]),
            'event_type': event["type"],
            'actor_id': event["actor"]["id"],
            'actor_login': event["actor"]["login"],
            'repo_id': event["repo"]["id"],
            'repo_name': event["repo"]["name"],
            'repo_url': event["repo"]["url"],
            'created_at': event["created_at"]
        })


# # Upload CSV file to S3
# s3 = boto3.client('s3')
# s3_key = f'{s3_prefix}/{csv_filename}'
# s3.upload_file(csv_filename, s3_bucket, s3_key)

# # Remove the local CSV file
# os.remove(csv_filename)

# print(f"CSV file uploaded to S3: s3://{s3_bucket}/{s3_key}")
