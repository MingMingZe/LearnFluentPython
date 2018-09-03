from abc import abstractmethod
from collections.abc import Iterable


class Iterator(Iterable):
    __slots__ = ()

    @abstractmethod
    def __next__(self):
        raise StopIteration

    def __iter__(self):
        return self

    @abstractmethod
    def __subclasshook__(cls, C):
        if cls is Iterable:
            if (any("__next__" in B.__dict__ for B in C.__mro__)
                    and any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
            return NotImplemented

if __name__ == '__main__':
    """这是源码，Interator的抽象类"""
    print("1")
