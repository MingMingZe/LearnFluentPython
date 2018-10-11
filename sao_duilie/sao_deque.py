from sao_duilie.SaoDLL import Sao_DLL, Full, Empty


# TODO 继承DLL实现deque
class Sao_deque(Sao_DLL):
    def __init__(self, maxsize):
        super().__init__(maxsize=maxsize)

    def de_append(self, item):
        if self.len() >= self.maxsize and self.maxsize is not None:
            raise Full("The sao_deque is full")
        return self.append(item)

    def de_append_left(self, item):
        if self.len() >= self.maxsize and self.maxsize is not None:
            raise Full("The sao_deque is full")
        return self.appendleft(item)

    def de_pop(self):
        if self.len() <= 0:
            raise Empty("The sao_deque is empty")
        tail = self.root.pre
        tail.pre.next = self.root
        self.root.pre = tail.pre
        self.length -= 1
        return tail.value

    def de_popleft(self):
        if self.len() <= 0:
            raise Empty("The sao_deque is empty")
        head = self.root.next
        self.root.next = head.next
        head.pre = self.root
        return head.value

    def new_pop(self):
        if self.len() <= 0:
            raise Empty("The sao_deque is empty")
        value = self.root.pre.value
        self.remove(value)
        return value