import requests

def extract_data(date_str):
    url = f'http://data.githubarchive.org/{date_str}.json.gz'
    r = requests.get(url)
    with open(f'{date_str}.json.gz', 'wb') as f:
        f.write(r.content)