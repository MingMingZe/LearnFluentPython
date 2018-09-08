import itertools


class ArithemticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.end)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            #降低处理浮点型
            result = self.begin + self.step * index


if __name__ == '__main__':
    # ap = ArithemticProgression(0, 1, 3)
    # print(list(ap))
    # ap = ArithemticProgression(1, .5, 3)
    # print(list(ap))
    # ap = ArithemticProgression(0, 1/3, 1)
    # print(list(ap))
    # from fractions import Fraction
    # ap = ArithemticProgression(0, Fraction(1, 3), 1)
    # print(list(ap))
    # from decimal import Decimal
    # ap = ArithemticProgression(0, Decimal('.1'), .3)
    # print(list(ap))

    gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
    print(list(gen))

