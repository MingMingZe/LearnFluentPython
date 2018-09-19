class MyFuture:
    def __init__(self):
        self.result = None

    def get(self):
        while(self.result is None):pass
        return self.result

    def set(self, item):
        self.result = item

