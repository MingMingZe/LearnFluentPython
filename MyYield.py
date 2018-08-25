def fibonacci(n):
    return fibonacci(n-2) + fibonacci(n-1) if n >= 2 else n


def gen_fibonacci2(n):
    m, a, b = 0, 0, 1
    while m < n:
        if m < 2:
            yield m
        elif m >= 2:
            a, b = b, a+b
            yield b
        m += 1


for i in range(9):
    print("normal：", fibonacci(i))

for item in gen_fibonacci2(9):
    print("gen_fibonacci2", item)
