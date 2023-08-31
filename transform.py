import gzip
import json
import csv
import os

def jsonl_to_csv(date_str):
    jsonl_file = f"data/{date_str}.json.gz"
    csv_file = f"csv/insights.github_events.{date_str.replace('-', '')}.csv"

    os.makedirs(os.path.dirname(csv_file), exist_ok=True)  # Create directory if it doesn't exist

    with gzip.open(jsonl_file, 'rt') as jf, open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow([
            'id',
            'actor_id',
            'actor_login',
            'actor_avatar_url',
            'repo_id',
            'repo_name',
            'author_email',
            'author_name',
            'created_at'
        ])  # headers
        for line in jf:
            event = json.loads(line)
            if event['type'] == 'PushEvent':
                writer.writerow([
                    event['id'],
                    event['actor']['id'],
                    event['actor']['login'],
                    event['actor']['avatar_url'],
                    event['repo']['id'],
                    event['repo']['name'],
                    event['created_at']
                ])
