import queue
import threading
from sao_thread.zao_queque import ZaoQueue


def zao_decoration(func):
    def inner():
        cond = threading.Condition()
        zaoq = ZaoQueue(5, cond)
        func()
    return inner

@zao_decoration
def test_zao_set_and_get(zaoq):
    for i in range(5):
        th = threading.Thread()
        zaoq.set(th)


if __name__ == '__main__':
    test_zao_set_and_get()
    queue.Queue()