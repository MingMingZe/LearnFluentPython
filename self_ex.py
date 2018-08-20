class Fruits:
    name = 'fruits'


class Apple:
    def __init__(self, taste):
        self.taste = taste


if __name__ == '__main__':
    apple = Apple('sweet')
    print('apple_instance dict', apple.__dict__, ' || apple_class dict', Apple.__dict__)
    apple.__dict__['shape'] = 'circle'
    print('apple_instance dic', apple.__dict__)
    print(dir(Apple))
