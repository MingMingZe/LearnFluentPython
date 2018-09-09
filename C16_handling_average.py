from collections import namedtuple

Result = namedtuple('Result', 'count average')

def average():
    total = 0.0
    count = 0
    average = None
    while True:
        try:
            term = yield
            total += term
            count += 1
            average = total / count
        except TypeError:
            return Result(count, average)



if __name__ == '__main__':
    coro_avg = average()
    next(coro_avg)
    coro_avg.send(10)
    coro_avg.send(30)
    coro_avg.send(6.5)
    try:
        coro_avg.send(None)
    except StopIteration as ex:
        result = ex.value
    print(result)
