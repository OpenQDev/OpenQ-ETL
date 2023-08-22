from dotenv import load_dotenv
import os
import pymysql
import json

load_dotenv()

# Read environment variables
db_host = os.environ['DB_HOST']
db_user = os.environ['DB_USER']
db_password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']
port = os.environ['PORT']
filepath = os.environ['FILEPATH']

# Function to load newline-separated JSON data from a file
def load_jsonl_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data

# Load data from test.json
github_data = load_jsonl_from_file(filepath)

ssl_config = {
    'ca': '/etc/ssl/cert.pem',
}

# Connect to the database
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=int(port),
    ssl=ssl_config
)

try:
    with connection.cursor() as cursor:
        # Insert events
        records_inserted = 0
        for event in github_data:
            id = int(event["id"])
            event_type = event["type"]
            actor_id = event["actor"]["id"]
            actor_login = event["actor"]["login"]
            repo_id = event["repo"]["id"]
            repo_name = event["repo"]["name"]
            repo_url = event["repo"]["url"]
            created_at = event["created_at"]
            
            cursor.execute("INSERT IGNORE INTO repositories (repo_id, repo_name, repo_url) VALUES (%s, %s, %s)", (repo_id, repo_name, repo_url))

            cursor.execute("INSERT IGNORE INTO users (actor_id, actor_login) VALUES (%s, %s)", (actor_id, actor_login))

            cursor.execute("INSERT INTO github_events (id, event_type, actor_id, repo_id, created_at) VALUES (%s, %s, %s, %s, %s)",
                           (id, event_type, actor_id, repo_id, created_at))
            
            connection.commit()

            # Update and print the record counter
            records_inserted += 1
            if records_inserted % 100 == 0:
                print(f"{records_inserted} records inserted.")

finally:
    connection.close()
