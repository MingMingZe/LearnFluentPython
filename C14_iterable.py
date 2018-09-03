import re
import reprlib


RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, item):
        return self.words[item]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(\"%s\")" % reprlib.repr(self.text)


if __name__ == '__main__':
    s = Sentence('"The time has come," the mingming said.')
    print(s)
    for word in s:
        print(word)
    print(tuple(s))
    from collections import abc
    print(isinstance(s, abc.Iterable))
    print(issubclass(Sentence, abc.Iterable))
