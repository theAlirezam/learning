from model import Article, database, Category


def create_table():
    database.create_tables([Article, Category])
