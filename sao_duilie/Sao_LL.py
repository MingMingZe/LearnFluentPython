class Node:
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class Linklist:
    def __init__(self, maxsize=None, value=None):
        self.maxsize = maxsize
        self.root = Node(value)
        self.length = 0
        self.tail = None

    def len(self):
        return self.length

    def append(self, value):
        if self.length >= self.maxsize and self.maxsize is not None:
            raise Exception("the LinkedList is Full")
        node = Node(value)
        if self.root.next is None:
            self.root.next = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def appendleft(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tail:
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
                self.length -= 1
                return cur_node.value
            cur_node = cur_node.next
        raise Exception("%s is not in this LQueue" % cur_node)

    def popleft(self):
        if self.root.next is None:
            raise Exception("the LinkedList is empty")
        head_node = self.root.next
        self.root.next = head_node.next
        self.length -= 1
        return head_node.value

    def find(self, item):
        index = 0
        for node in self.iter_node():
            if item == node.value:
                return index
            index += 1
        index = -1
        raise index

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


