import requests
from config import url2, rules
import json

unic = ''


def get_data():
    is_respond = requests.get(url2)
    if is_respond.status_code == 200:
        return json.loads(is_respond.text)

    return None


def archive_to_dir(filename, data):
    with open(f'directory/{filename}.json', 'w') as f:
        f.write(json.dumps(data))


def send_email(subject, text):
    text = json.dumps(text)


res = get_data()
if rules['archive']:
    archive_to_dir(res['time_table'], res['data'])
if rules['send_email']:
    send_email('test1', res['data'])
