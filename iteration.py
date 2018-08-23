from collections.abc import Iterator


class Bus:
    def __init__(self, passengers):
        self.passengers = passengers

    def __iter__(self):
        return iter(self.passengers)


class MyIterator(Iterator):
    def __init__(self, passengers):
        self.index = 0
        self.passengers = passengers

    def __next__(self):
        try:
            passenger = self.passengers[self.index]
        except IndexError:
            raise StopIteration


if __name__ == '__main__':
    passengers = ["mingming", "ziqiang", "zili"]
    bus = Bus(passengers)
    for item in bus:
        print(item)

"""
打印结果：
mingming
ziqiang
zili
"""
