import time
from threading import Thread


class Thread1(Thread):
    def __init__(self, name):
        super().__init__(name)

    print("class thread1 is run")
    time.sleep(2)
    print("class thread1 is stopped")


class Thread2(Thread):
    def __init__(self, name):
        super().__init__(name)

    print("class thread2 is run")
    time.sleep(2)
    print("class thread2 is stopped")


if __name__ == '__main__':
    thread1 = Thread1("thread 1")
    thread2 = Thread2("thread 2")
    t0 = time.time()
    thread1.start()
    thread2.start()
    print("last time {time}".format(time=time.time()-t0))

