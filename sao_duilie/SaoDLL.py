class Node:
    def __init__(self, value=None, pre=None, next=None):
        self.value, self.pre, self.next = value, pre, next


class Full(Exception):
    pass


class Empty(Exception):
    pass


class Sao_DLL:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        self.root = node
        self.root.pre, self.root.next = node, node
        self.length = 0

    def len(self):
        return self.length

    def append(self, item):
        if self.length >= self.maxsize and self.maxsize is not None:
            raise Full("The Sao_dequeue is full, exception in ")
        node = Node(value=item)
        tail = self.root.pre
        tail.next = node
        node.pre = tail
        node.next = self.root
        self.root.pre = node
        self.length += 1

    def appendleft(self, item):
        if self.length >= self.maxsize and self.maxsize is not None:
            raise Full("The Sao_dequeue is full, exception in %s" % self.__name__)
        node = Node(item)
        if self.root.next is self.root:
            self.root.next = node
            node.next = self.root
            self.root.pre = node
            node.pre = self.root
        else:
            head = self.root.next
            head.pre = node
            node.next = head
            self.root.next = node
            node.pre = self.root
        self.length += 1

    # def remove(self, node):
    #     if node is self.root:
    #         return
    #     else:
    #         node.pre.next = node.next
    #         node.next.pre = node.pre
    #     self.length -= 1
    #     return node

    def remove(self, value):
        for item in self.iter_node():
            if item.value == value:
                item.pre.next = item.next
                item.next.pre = item.pre
            self.length -= 1
            return value

    def iter_node(self):
        curr_node = self.root.next
        while curr_node is not self.root.pre:
            yield curr_node
            curr_node = curr_node.next
        yield curr_node

    def iter_value(self):
        curr_node = self.root.next
        while curr_node is not self.root.pre:
            yield curr_node.value
            curr_node = curr_node.next
        yield curr_node.value

    def __iter__(self):
        for i in self.iter_node():
            yield i

    def iter_reverse(self):
        curr_node = self.root
        while curr_node is not self.root:
            yield curr_node
            curr_node = curr_node.pre

    def iter_reverse_value(self):
        curr_node = self.root.pre
        while curr_node is not self.root:
            yield curr_node.value
            curr_node = curr_node.pre
