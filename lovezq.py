import time
from functools import lru_cache


def clock(func):
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        args_str = ''.join(repr(arg) for arg in args)
        print("[%0.8fs]%s(%s) -> %r" % (elapsed, name, args_str, result))
        return result

    return clocked


@lru_cache()
@clock
def fibonacci(n):
    return fibonacci(n - 2) + fibonacci(n - 1) if n >= 2 else n


if __name__ == '__main__':
    print(fibonacci(10))
    print('nihao')
