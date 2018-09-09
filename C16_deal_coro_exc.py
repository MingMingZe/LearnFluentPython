class DemoException(Exception):
    """异常类"""
def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print("***DemoException handle.Coroutine……")
        else:
            print("->coroutine recived:{!r}".format(x))
        finally:
            print("-> coroutine ending")

if __name__ == '__main__':
    exc_coro = demo_exc_handling()
    next(exc_coro)
    exc_coro.send(11)
    exc_coro.send(22)
    exc_coro.throw(DemoException)
    # exc_coro.close()
    from inspect import getgeneratorstate
    print(getgeneratorstate(exc_coro))
