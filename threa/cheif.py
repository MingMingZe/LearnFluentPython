from threading import Thread

class chef(Thread):
    def __init__(self, cook_menus):
        Thread.__init__(self)
        self.future = None
        self.cook_menus = cook_menus

    def run(self):

        while self.cook_menus is not None:
            # 获取future和函数对象，为啥没有执行这个函数对象呢？
            #执行是线程执行的，对啊，你现在不就在线程中吗
            # 执行过的结果为啥没有放进future？
            #menu 就是一个函数啊
            future, cook_mennu=self.cook_menus.get()
            self.future = future
            result = cook_mennu()
            self.future.set_menu(result)
            print("chef finshing")





