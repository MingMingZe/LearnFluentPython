import queue
import threading


class SaoQueue:
    def __init__(self, maxlength):
        self.L = []
        self.maxlength = maxlength
        self.lock = threading.Lock()

    def set(self, list):
        if self.isfull():
            raise Exception("index is out of range")
            # self.lock.acquire(blocking=True, timeout=5.0)
        else:
            for item in list:
                self.L.append(item)


    def __len__(self):
        return len(self.L)

    def get(self, i):
        if i < 0 or i > len(self.L) - 1:
            raise Exception("index out of range")
        else:
            return self.L[i]

    def __iter__(self):
        for i in self.L:
            yield i


    def concat(self, sao):
        for i in sao:
            self.L.append(i)
        return self.L


    def isempty(self):
        if len(self.L) == 0:
            return True
        else:
            return False

    def isfull(self):
        if len(self.L) == self.maxlength:
            return True
        else:
            return False

    def top(self):
        if self.isempty():
            raise Exception("the queue is empty that you can't top()")
        else:
            return self.L[len(self.L)-1]

    def pop(self):
        # TODO 实现同步：多线程进来同步，如果队列为空则等待,弹出后通知push等待线程
        if self.isempty():
            raise Exception("the SaoQueue is empty can't pop")
        else:
            return self.L.pop()

    def push(self, value):
        # TODO 实现同步：多线程进来同步，如果队列已满则等待，放入成功后通知pop线程

        if len(self.L) >= self.maxlength:
            raise Exception("the SaoQueue is full")
        else:
            self.L.append(value)

    def __str__(self):
        return str(self.L)

    def endequeue(self, item):
        if self.isfull():
            raise Exception("the SaoQueue is full")
        else:
            self.L =  [item] + self.L
            return self.L

    def dequeue(self):
        if self.isempty():
            raise Exception("there is no pop0")
        else:
           return self.L.pop(0)




if __name__ == '__main__':
    sq = SaoQueue(8)
    # set测试
    sq.set([i for i in range(5, 10)])
    # 测试iter
    for i in sq:
        print(i)
    # len测试
    print("len测试", sq.__len__())
    # get测试
    print("get测试", sq.get(2))
    # concat测试
    sq1 = SaoQueue(5)
    sq1.set([i for i in range(11,13)])
    print("concat测试", sq.concat(sq1))
    # isempty测试
    print("isempty测试 sq", sq.isempty())
    sq2 = SaoQueue(1)
    print("isempty测试 sq2", sq2.isempty())
    print("top测试", sq.top())
    print("pop测试", sq.pop())
    for i in sq:
        print(i)
    # push进去22
    sq.push(22)
    print("push测试", sq)
    print("enqueque:", sq.endequeue(33))
    sq.dequeue()
    print("dequeue:", sq)


