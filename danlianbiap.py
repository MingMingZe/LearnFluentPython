class Node:
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class Linklist:
    def __init__(self, maxsize=None, value=None):
        self.maxsize = maxsize
        self.root = Node(value)
        self._item = []
        self.length = 0
        self.tatil = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.length > self.maxsize and self.maxsize is None:
            raise Exception("the LinkedList is Full")
        node = Node(value)
        tatilnode = self.tatil
        if tatilnode is None:
            self.root = node
        else:
            tatilnode.next = node
        self.tatil = tatilnode
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tatil:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for i in self.iter_node():
            yield i

    def remove(self, value):
        pre_node = self.root
        cur_node = self.root.next
        while cur_node.value is not None:
            if cur_node.value == value:
                pre_node.next = cur_node.next
                del cur_node
                self.length -= 1
                return cur_node

    def popleft(self):
        if self.root.next is None:
            raise Exception("the LinkedList is empty")
        head_node = self.root.next
        self.root.next = head_node.next
        self.length += 1
        del head_node
        return head_node

    def find(self, value):
        index = 0
        for node in self.iter_node():
            if value == node.value:
                return index
            index += 1
        return Exception("%s is not in the LinkedList" % value)

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
