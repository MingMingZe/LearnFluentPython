import random
import time
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor


def get_html(t):
    time.sleep(t)
    print("get html{} successfuly".format(t))
    return t

# executor.submit
executor = ThreadPoolExecutor(max_workers=2)
task1 = executor.submit(get_html, (3))
task2 = executor.submit(get_html, (2))






if __name__ == '__main__':
    # executor.submit()
    print(task1.done())
    print(task2.cancel())#false:max_worker=2一进来线程池就被执行了
    time.sleep(3)
    print(task1.done())

    # future.as_completed
    all_task = [executor.submit(get_html, t) for t in [2, 3, 1]]
    for future in as_completed(all_task):
        data = future.result()
        print("as_completed! html{}".format(data))

    for future0 in executor.map(get_html, [0.2, 0.1, 0.3]):
        print("map html{}".format(future0))#直接返回future.result()






