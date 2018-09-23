import threading
import time
from collections import deque


class BlockQueue:
    def __init__(self, maxsize=0):
        self.mutex = threading.Lock()
        self.maxsize = maxsize
        self.not_full = threading.Condition(self.mutex)
        self.not_empty = threading.Condition(self.mutex)
        self.all_task_done = threading.Condition(self.mutex)
        self.unfinished = 0

    def task_done(self):
        with self.all_task_done:
            unfinish = self.unfinished - 1
            if unfinish <= 0:
                if unfinish < 0:
                    raise Exception("The number of calls to task_done() is greater than the number of queue elements")
                self.all_task_done.notify_all()
            self.unfinished = unfinish

    def join(self):
        with self.all_task_done:
            while self.unfinished:
                self.all_task_done.wait()

    def _init(self):
        self.queue = deque()

    def _size(self):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        self.queue.popleft()

    def put(self, item, block=True, timeout=None):
        with self.not_full:
            if self.maxsize > 0:
                if not block:
                    if self._size() >= self.maxsize:
                        raise Exception("The BlockQueue is full")
                elif timeout is not None:
                    self.not_full.wait()
                elif timeout < 0:
                    raise Exception("The timeout period cannot be negative")
                else:
                    endtime = time.time() + timeout
                    while self._size() >= self.maxsize:
                        remaining = endtime - time.time()
                        if remaining <= 0.0:
                            raise Exception("The BlockQueue is full")
                        self.not_full.wait(remaining)
                    self.queue.append(item)
                    self.unfinished += 1
                    self.not_empty.notify()

    def get(self, block=True, timeout=None):
        with self.not_empty:
            if not block:
                if self._size() <= 0:
                    raise Exception("The queue is empty and you can't call get ()")
                elif timeout is None:
                    while not self._size():
                        self.not_empty.wait()
                elif timeout < 0:
                    raise ValueError("The timeout cannot be an integer")
                else:
                    endtime = time.time() + timeout
                    remaining = endtime - time.time()
                    if remaining <= 0.0:
                        raise Exception("The BlockQueue is empty")
                    self.not_empty.wait(remaining)
                item = self._get()
                self.not_full.notify()
                return item

    def put_notwait(self, item):
        return self.put(item, False, None)

    def get_notwait(self):
        return self.get(False, None)
