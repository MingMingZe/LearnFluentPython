import queue
from threa.cheif import chef
from threa.my_token import my_token


class Waiter:
    def __init__(self, maxlen=5):
        self.chefs = []
        self.maxnum = maxlen
        self.menus = queue.Queue(10)
        self.new_thread()

    def put_task(self, cook):
        token = my_token()
        task = (token, cook)
        self.menus.put(task)
        return token

    """
        def submit(fn):
            f = MyFuture()
            th = MyThread(fn, f)
            th.start()
            return f

    """
    def new_thread(self):
        i = 0
        while i < self.maxnum:
            chushi = chef(self.menus)
            chushi.setDaemon(True)
            chushi.start()
            self.chefs.append(chushi)
            i += 1

    # def stop_thread(self):
    #     for thread in self.chefs:
    #         thread.
