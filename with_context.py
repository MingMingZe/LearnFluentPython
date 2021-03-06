class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __enter__(self):
        """
        1、必须实现此函数
        2、通常用于获取资源
        3、会自动被调用
        4、通常要return self
        """
        print("enter")
        return self

    def add(self, other):
        """
        1、此函数用于实现所需要的功能
        2、通常要return
        """
        self.a += other.a
        self.b += other.b
        return self.a, self.b

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        1、必须实现此函数
        2、通常用于释放资源
        3、会自动被调用
        4、参数记录异常信息默认是None
        5、没有异常则执行剩下的代码
        """
        print("exit")


if __name__ == '__main__':
    vector1 = Vector(2, 3)
    vector2 = Vector(4, 5)
    print(vector1.add(vector2))

with Vector(7, 8) as vector3:
    print(vector3.add(vector1))

"""
打印结果:

(6, 8)
enter
(13, 16)
exit
"""
print("///////////")

# 利用装饰器contextmanager
from contextlib import contextmanager


@contextmanager
def dealfile():
    """
    yield前面放__enter__的内容不用return，yield后面放__exit__的内容
    :return:
    """
    print("hello")
    yield {}
    print("bye")


with dealfile():
    print("have a good time")

"""
打印结果：
hello
have a good time
bye
"""
