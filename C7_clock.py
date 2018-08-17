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



############result######################
[0.00000000s]fibonacci(0) -> 0
[0.00000000s]fibonacci(1) -> 1
[0.00000000s]fibonacci(2) -> 1
[0.00000000s]fibonacci(3) -> 2
[0.00000000s]fibonacci(4) -> 3
[0.00000000s]fibonacci(5) -> 5
[0.00000000s]fibonacci(6) -> 8
[0.00000000s]fibonacci(7) -> 13
[0.00000000s]fibonacci(8) -> 21
[0.00000000s]fibonacci(9) -> 34
[0.00000000s]fibonacci(10) -> 55
55
