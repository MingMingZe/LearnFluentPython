import queue
import threading


class ZaoQueue:
    def __init__(self, maxlen, condition):
        self.maxlength = maxlen
        self.cond = condition
        self.queue = queue.Queue()

    def get(self):
        if self.cond.acquire():
            while self.queue.empty():
                self.cond.wait()
            ele = self.queue.get()
            self.cond.notify()
            self.cond.release()
            return ele


    def set(self, item):
        if self.cond.acquire():
            while self.queue.qsize() >= self.maxlength:
                self.cond.wait()
                self.queue.put(item)
            self.cond.notify()
            self.cond.release()

if __name__ == '__main__':
    cond = threading.Condition()
    zaoq = ZaoQueue(5, cond)
    for i in range(5):
        th = threading.Thread()
        zaoq.set(th)

