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


# 打印结果：
# normal： 0
# normal： 1
# normal： 1
# normal： 2
# normal： 3
# normal： 5
# normal： 8
# normal： 13
# normal： 21
# gen_fibonacci2 0
# gen_fibonacci2 1
# gen_fibonacci2 1
# gen_fibonacci2 2
# gen_fibonacci2 3
# gen_fibonacci2 5
# gen_fibonacci2 8
# gen_fibonacci2 13
# gen_fibonacci2 21
