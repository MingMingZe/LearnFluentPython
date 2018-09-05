class ArithemticProgression:
    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.end)(self.begin)
        forever = self.end is None
        index = 0
        while forever or index < self.end:
            yield result
            index += 1
            #降低处理浮点型
            result = self.begin + self.step * index

