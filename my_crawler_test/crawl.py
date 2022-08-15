import json
from abc import abstractmethod, ABC
from config import LINK, CITIES
import requests
from bs4 import BeautifulSoup

from my_crawler_test.parser import CrawlParser


class CrawlBase(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def store(self, data):
        pass

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
        except requests.HTTPError:
            return None
        print(response.status_code, response.url)
        return response


class LinkCrawler(CrawlBase):

    def find_links(self, html_doc):
        # content = soup.find('div', attrs={'class': 'content'})
        # adv_list = soup.find_all('li', attrs={'class': 'result-row'})
        soup = BeautifulSoup(html_doc, 'html.parser')
        advs = soup.find_all('a', attrs={'class': 'hdrlnk'})
        return advs

    def start_crawl_city(self, url):
        crawl = True
        start = 0
        adv_list = list()

        # while crawl:
        rspnd = self.get(url + str(start))
        new_links = self.find_links(rspnd.text)
        adv_list.extend(new_links)
        # start += 120
        crawl = bool(len(new_links))
        # if start > 100:
        #     crawl = False
        return adv_list

    def start(self):
        adv_list = list()
        for city in CITIES:
            links = self.start_crawl_city(LINK.format(city))
            print(city + "  " + str(len(links)))
            adv_list.extend(links)
        self.store([ki.get('href') for ki in adv_list])

    def store(self, data):
        with open("Data.json", 'w') as f:
            f.write(json.dumps(data))


class DataCrawler(CrawlBase):
    def __init__(self):
        self.links = self.__loadlinks()
        self.parser = CrawlParser()

    @staticmethod
    def __loadlinks():
        with open("Data.json", "r") as f:
            links = json.loads(f.read())
        return links

    def start(self):
        for link in self.links:
            response = self.get(link)
            data = self.parser.parse(response)
            print(data)

    def store(self, data):
        with open("Data.json", 'w') as f:
            f.write(json.dumps(data))




