import time
import threading


def thread_A():
    print("threadA is started")
    time.sleep(2)
    print("ThreadA is stopped")


def thread_B():
    print("threadB is started")
    time.sleep(2)
    print("ThreadB is stopped")


if __name__ == '__main__':
    thread_a = threading.Thread(target=thread_A)
    thread_b = threading.Thread(target=thread_B)
    # thread_a.thread_setDaemon(True)
    # thread_b.setDaemon(True)
    t0 = time.time()
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()
    t = time.time() - t0
    print("运行时长：", t)
