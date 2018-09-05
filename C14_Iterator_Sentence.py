class IteratorSentence:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return self


class Sentence_v1:
    def __init__(self):
        super(Sentence_v1, self).__init__()

    def __iter__(self):
        for word in super().words:
            yield word
        return
