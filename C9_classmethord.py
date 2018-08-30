class Demo:
    @classmethod
    def klassmeth(*args):
        return args
    @staticmethod
    def staticmeth(*args):
        return args

if __name__ == '__main__':
    print("Demo.klassmeth():", Demo.klassmeth(), "Demo.klassmeth(\"mingming\"):", Demo.klassmeth("mingming"))
    print("Demo.staticmeth():", Demo.staticmeth(), "Demo.staticmeth(\"mingming\"):", Demo.staticmeth("mingming"))