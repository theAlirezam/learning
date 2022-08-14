import requests
from bs4 import BeautifulSoup


def get_page(url, start=0):
    try:
        response = requests.get(url+str(start))
    except:
        return None
    # print(response.status_code, response.url)
    return response


def find_links(html_doc):
    # content = soup.find('div', attrs={'class': 'content'})
    # adv_list = soup.find_all('li', attrs={'class': 'result-row'})
    soup = BeautifulSoup(html_doc, 'html.parser')
    advs = soup.find_all('a', attrs={'class': 'hdrlnk'})
    return advs


def start_crawl(url):
    crawl = True
    start = 0
    adv_list = list()

    while crawl:
        rspnd = get_page(url, start)
        new_links = find_links(rspnd.text)
        adv_list.extend(new_links)
        start += 120
        crawl = bool(len(new_links))
        if start > 600:
            crawl = False
    return adv_list


if __name__ == "__main__":
    LINK = "https://{}.craigslist.org/search/apa?s="
    CITIES = ['newyork', 'toronto', 'london', 'munich']

    for city in CITIES:
        links = start_crawl(LINK.format(city))
        print(city + "  " + str(len(links)))




