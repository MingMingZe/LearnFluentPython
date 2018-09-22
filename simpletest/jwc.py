import requests
from PIL import Image
from requests import Response
from bs4 import BeautifulSoup
import http.cookies


class Login:
    def __init__(self):
        self.url = "http://172.20.139.153/loginAction.do"
        self.headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Host': '172.20.139.153',
            'Referer': 'http://172.20.139.153/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'Cookie': 'JSESSIONID = abfpIolEEhLbc5ubux-xw',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.session = requests.session()

    def login(self, username, password):
        resp = Response()
        form = {
            'zjh1': '',
            'tips': '',
            'lx': '',
            'evalue': '',
            'eflag': '',
            'fs': '',
            'dzslh': '',
            'zjh': username,
            'mm': password,
            'v_yzm': self.get_verification()
        }
        try:
            resp = self.session.post(self.url, headers=self.headers, data=form)
        except Exception as e:
            print(repr(e))
        print(resp.text)
        return resp.status_code


    def get_verification(self):
        imgurl = 'http://172.20.139.153/validateCodeAction.do'
        mysession = requests.Session()
        html = mysession.get(imgurl, timeout=60 * 4)
        checkwxxxcode_style = mysession.get(imgurl, timeout=60 * 40)
        with open('checkwxxxcode_style.png', 'wb') as f:
            f.write(checkwxxxcode_style.content)
        check_img = Image.open("checkwxxxcode_style.png")
        check_img.show()
        verification = input('请输入验证码')
        return verification

    # def get_classinfo(self):
    #     url = 'http://172.20.139.153/xkAction.do?actionType=6'
    #     soup = BeautifulSoup(resp.text, 'lxml')
    #     cla = soup.find_all("td")
    #     print(cla)
