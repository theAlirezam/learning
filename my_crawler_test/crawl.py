import json
import requests
from abc import abstractmethod, ABC
from config import LINK, CITIES, STORAGE_TYPE
from bs4 import BeautifulSoup
from storage import MongoStorage, FileStorage

from my_crawler_test.parser import CrawlParser


class CrawlBase(ABC):

    def __init__(self):
        self.Storage = self.__set_storage()
        self.cp = CrawlParser()

    def __set_storage(self):
        if STORAGE_TYPE == 'mongodb':
            return MongoStorage()
        return FileStorage()

    @abstractmethod
    def start(self, store=False):
        pass

    @abstractmethod
    def store(self, data, filename):
        pass

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
        except requests.HTTPError:
            return None
        # print(response.status_code, response.url)
        return response


class LinkCrawler(CrawlBase):
    # called super withot init sus for a raise
    def __init__(self):
        super().__init__()

    def find_links(self, html_doc):
        # content = soup.find('div', attrs={'class': 'content'})
        # adv_list = soup.find_all('li', attrs={'class': 'result-row'})
        soup = BeautifulSoup(html_doc, 'html.parser')
        advs = soup.find_all('a', attrs={'class': 'hdrlnk'})
        return advs

    def start_crawl_city(self, url):
        # crawl = True
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

    def start(self, store=False):
        adv_list = list()
        for city in CITIES:
            links = self.start_crawl_city(LINK.format(city))
            print(city + "  " + str(len(links)))
            adv_list.extend(links)
        if store:
            self.store([ki.get('href') for ki in adv_list])
        return adv_list

    def store(self, data, *args):
        self.Storage.store(data, 'Data')


class DataCrawler(CrawlBase):
    def __init__(self):
        super().__init__()
        self.links = self.__loadlinks()
        self.parser = CrawlParser()

    @staticmethod
    def __loadlinks():
        with open("files/Data.json", "r") as f:
            links = json.loads(f.read())
        return links

    def start(self, store=False):
        for link in self.links:
            response = self.get(link)
            data = self.parser.parse(response.text)

            if store:
                self.store(data, data.get('post_id', 'sample'))

            print(data)

    def store(self, data, filename):
        self.Storage.store(data, filename)


class ImageDownloader(CrawlBase):
    def __init__(self):
        super().__init__()
        self.advertisement = self.__load_advertisements()

    @staticmethod
    def get(link):
        try:
            response = requests.get(link, stream=True)
        except requests.HTTPError:
            return None
        # print(response.status_code, response.url)
        return response

    def start(self, store=False):
        for ad in self.advertisement:
            counter = 1
            for img in self.advertisement['images']:
                response = self.get(img)
                counter += 1
                self.store(response, ad['post_id'], counter)

    def store(self, data, id, num):
        filename = f'{id}-{num}'
        return self.save_to_disk(data, filename)

    def __load_advertisements(self):

        images = self.cp.data['images']
        print(images)
        return images

    def save_to_disk(self, response, filename):
        with open(f'files/images/{filename}.jpg', 'ab') as f:
            f.write(response.content)
            for _ in response.iter_content():
                f.write(response.content)

