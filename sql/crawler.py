from bs4 import BeautifulSoup
from model import Article, Category
import requests


def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1')

    body = soup.find('h2', attrs={'class': 'detOzet'})
    if body and title is not None:
        export = {'title': title.text, 'body': body.text}
        print(export)
        return export
    return {'title': '', 'body': ''}


def get_links():
    response = requests.get('https://www.trthaber.com/')
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    links_list = list()
    for link in links:
        href = link.attrs.get('href')
        if href is not None and href.startswith('haber/') and len(href) > 23:
            news = 'https://www.trthaber.com/' + href
            links_list.append(news)
    #######################
    return links_list


# articles = Article.select().where(Article.is_completed == False)
# for article in articles:
#     print(article.id)
#     title = get_data(article.url)
