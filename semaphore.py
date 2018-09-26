import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(0.01)
        print("get html text")
        self.sem.release()


class UrlProductor(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html = HtmlSpider("www.xx.com", self.sem)
            html.start()


if __name__ == '__main__':
    Sem = threading.Semaphore(3)
    url_producer = UrlProductor(Sem)
    url_producer.start()