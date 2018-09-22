from sao_thread.sao_Queue import SaoQueue


def new_saoque(fun):
    def inner():
        sq = SaoQueue(5)
        fun(sq)
        print(fun.__name__ + ":" + str(sq))
    return inner


@new_saoque
def tes_set(sq):
    # 测试set()
    list = [1, 2, 3]
    sq.set(list)
    sq.set([1, 2])
    # print(sq)

@new_saoque
def tes_push(sq):
    for i in range(5):
        sq.push(i)
    # print(sq)

@new_saoque
def tes_pop(sq):
    sq.set([i for i in range(1)])
    print(sq)
    sq.pop()
    # print(sq)
    # TODO sq.pop()

@new_saoque
def tes_contact(sq):
    sq1 = SaoQueue(2)
    sq1.set([1,3])
    sq.set([2, 4])
    sq.concat(sq1)

@new_saoque
def tes_top(sq):
    sq.set([1,2,3])
    print(sq.top())

@new_saoque
def tes_enqueue(sq):
    sq.set([1, 2, 3,4])
    sq.endequeue(88)
    # TODO sq.endequeue(888)

@new_saoque
def tes_dequeue(sq):
    sq.set([i for i in range(1)])
    sq.dequeue()
    # TODO sq.dequeue()


def to_do():
   pass

if __name__ == '__main__':
    tes_set()
    tes_push()
    tes_pop()
    tes_contact()
    tes_top()
    tes_enqueue()
    tes_dequeue()

