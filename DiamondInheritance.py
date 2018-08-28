class A:
    def ping(self):
        print('class_A ping:', self)


class B(A):
    def pong(self):
        print('class_B pong:', self)


class C(A):
    def pong(self):
        print('class_C pong:', self)


class D(B, C):
    def ping(self):
        super().ping()
        print('class_D ping', self)

    def pingpong(self):
        self.ping()
        A.ping(self)
        self.pong()
        super().pong()
        C.pong(self)  # 直接调用父类方法时，要把实例作为显式参数


if __name__ == '__main__':
    d = D()
    d.pong()
    # 直接调用父类方法时，要把实例作为显式参数
    C.pong(d)
    print(D.__mro__)
    d.pingpong()
