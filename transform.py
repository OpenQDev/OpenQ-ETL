import json
import csv

def jsonl_to_csv(jsonl_file, csv_file):
    with open(jsonl_file, 'r') as jf, open(csv_file, 'w', newline='') as cf:
        writer = csv.writer(cf)
        writer.writerow(['event_id', 'actor_id', 'repo_id', 'created_at'])  # headers
        for line in jf:
            event = json.loads(line)
            if event['type'] == 'PushEvent':
                writer.writerow([event['id'], event['actor']['id'], event['repo']['id'], event['created_at']])
