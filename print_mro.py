def print_mro(cls):
    print(",".join(c.__name__ for c in cls.__mro__))


if __name__ == '__main__':
    import numbers
    print_mro(numbers.Integral)
    import io
    print_mro(io.BytesIO)
    print_mro(io.TextIOWrapper)
    