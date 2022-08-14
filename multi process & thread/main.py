import multiprocessing
import queue
import time

#
# q = multiprocessing.Queue()
#
#
# def worker(num):
#     while True:
#         job_id = q.get()
#         time.sleep(3)
#         print(f"worker {num} & job id {job_id}")
#
#         if q.empty():
#             break


# if __name__ == "__main__":

# for i in range(13):
#     q.put(i)
# process_list = list()
# for i in range(4):
#     p = multiprocessing.Process(target=worker, args=(i,))
#     process_list.append(p)
#     p.start()
#
# print('all tasks finished')
# for pr in process_list:
#     pr.join()
#
