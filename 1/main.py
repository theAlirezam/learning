import requests
from config import url2
import json


def get_data():
    irespond = requests.get(url2)
    if irespond.status_code == 200:
        return json.loads(irespond.text)
    return None


def archive_to_dir(filename, data):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(data))


res = get_data()
archive_to_dir('tst1', res['data'])
print(get_data())


print('hi')

# urll = "https://api.apilayer.com/fixer/convert?to={to}&from={from}&amount={amount}"
#
# payload = {}
# headers = {
#     "apikey": "oX92FSLGD0HlitzTTjbeFSSxvqHKUPYI"
# }
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# status_code = response.status_code
# result = response.text
# # print(result)


