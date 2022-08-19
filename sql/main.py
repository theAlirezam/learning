from db import create_table
from crawler import get_links, get_data
from model import database, Article, Category


def create_database():
    create_table()


def get_the_links():
    cat = Category.create(name='sport')
    for link in get_links():
        article = Article.create(url=link, category=cat)
        print(article.id)


def add_data():
    # articles = Article.create()
    articles = Article.select().where(Article.is_completed == False)
    for article in articles:
        data = get_data(article.url)
        article.title = data['title']
        article.body = data['body']
        article.is_completed = True
        article.save()
        print(article.id)


if __name__ == "__main__":
    # create_database()
    # get_the_links()
    add_data()
