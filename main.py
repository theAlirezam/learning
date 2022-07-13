import requests
from config import url, API_KEY
import json


def get_rates():
    respond = requests.get(url + API_KEY)
    if respond.status_code == 200:
        return json.loads(respond.text)
    return None


def archive_to_dir(filename, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


res = get_rates()
# archive_to_dir(res['timestamp'], res['rates'])
print(get_rates())