import inspect


def simple_coroutine(a):
    print('-> started: a = ', a)
    b = yield a
    print('-> received: b =', b)
    c = yield b
    print('-> received: c =', c)


if __name__ == '__main__':
    coro = simple_coroutine(1)
    print(inspect.getgeneratorstate(coro))
    next(coro)
    coro.send(2)
    print(inspect.getgeneratorstate(coro))
    next(coro)
    coro.send(3)
    inspect.getgeneratorstate(coro)
    next(coro)
