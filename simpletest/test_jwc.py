import unittest
import requests
from simpletest.jwc import Login


class LoginTest(unittest.TestCase):
    def test_verification(self):
        lo = Login()
        lo.get_verification()
        # self.assertEquals('5678', lo.form['v_yzm'])

    def test_login(self):
        lo = Login()
        status_code = lo.login('2016133002', '101723')
        self.assertEquals(200, status_code)

    def test_get(self):
        resp = requests.session().get("http://172.20.139.153/loginAction.do")
        print(resp.text)

    def test_classinfo(self):
        pass
