from sao_duilie.Sao_LL import Linklist


class Full(Exception):
    pass


class Empty(Exception):
    pass


class MyQueue:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._list = Linklist(self.maxsize)

    def __len__(self):
        return self._list.len()

    def push(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Full("MyQueue is full")
        return self._list.append(value)

    def pop(self):
        if len(self) <= 0:
            raise Empty("MyQueue is empty")
        return self._list.popleft()

