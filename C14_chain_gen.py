def chain(*iterables):
    for i in iterables:
            yield from i


if __name__ == '__main__':
    s = 'ABC'
    t = tuple(range(3))
    print(list(chain(s, t)))