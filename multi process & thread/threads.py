import queue
import threading
import time

import requests

q = queue.Queue()


def worker(number):
    time.sleep(2)
    print()


def get_page(num):
    while True:
        url = q.get()

        try:
            respond = requests.get(url)
        except:
            print('ERROR!')
        print(f"worker {num}\t link {url}\t queue size {q.qsize()}")
        q.task_done()
        if q.empty():
            break


if __name__ == "__main__":

    links = [
                "https://farsroid.com",
                "https://google.com",
                "https://yasdl.com",
            ] * 3

    for link in links:
        q.put(link)

    threads_list = list()


    def multi_thread():

        for i in range(3):
            t = threading.Thread(target=get_page, args=(i,))
            threads_list.append(t)

            t.start()
