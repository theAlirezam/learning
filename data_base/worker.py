import sys
from redis import Redis

client = Redis()


def watch_links(name):
    print(f'{name} has started')
    while True:
        link = client.blpop('links')
        print(link)


if __name__ == "__main__":
    watch_links(sys.argv[1])
