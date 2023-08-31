import requests
import os

def extract_data(date_str):
    url = f"https://data.gharchive.org/{date_str}.json.gz"
    response = requests.head(url)
    if response.status_code == 404:
        return False
    else:
        os.system(f"wget {url} -O data/{date_str}.json.gz")
        return True