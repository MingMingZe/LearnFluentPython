import functools
import itertools
import numbers
import operator
import random
import reprlib
from array import array
import math


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    # def __eq__(self, other):
    #     if len(self) != len(other):
    #         return False
    #     for a, b in zip(self, other):
    #         if a != b:
    #             return False
    #     return True

    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        return functools.reduce(operator.xor, hashes)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __format__(self, format_spec=''):
        if format_spec.endswith('h'):
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, format_spec) for c in coords)
        return outer_fmt.format(",".join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = '{.__name__}indices must be integral'
            raise TypeError(msg.format(cls))

    def __len__(self):
        return len(self._components)

    shortcut_name = 'xyzmn'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_name.find(name)
            if 0 <= pos <= len(self._components):
                return self._components[pos]
        msg = '{.__name__!r}object has no attribute{!r}'
        raise AttributeError(msg.format(cls, name))


if __name__ == '__main__':
    v1 = Vector([random.random() for i in range(5)])
    print("v1:", v1, "v1.m:", v1.m)
    print("format(v1, '.3eh')", format(v1, '.3eh'))
    print("format(v1, '.2f')", format(v1, '.2f'))
