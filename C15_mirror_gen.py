import contextlib


@contextlib.contextmanager
def loooking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''
    try:
        yield "JABBERWOCKY"
    except ZeroDivisionError:
        msg = 'please do not divide by zero'
    finally:
        sys.stdout.write = original_write
        if msg:
            print(msg)


if __name__ == '__main__':
    with loooking_glass() as what:
        print("mingming, qiangqiang, lili, minmin")
        print(what)
    print("what:", what)
