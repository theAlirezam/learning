import requests
from config import url, API_KEY
respond = requests.get(url + API_KEY)
print(respond)