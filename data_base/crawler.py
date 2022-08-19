import requests
from bs4 import BeautifulSoup
from redis import Redis

client = Redis()


def get_links(url='https://varzesh3.com'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for link in soup.find_all('a'):
        client.rpush('links', link.getText('href'))


if __name__ == "__main__":
    get_links()
