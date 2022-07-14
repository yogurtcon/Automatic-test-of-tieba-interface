import unittest
from public.common import *


class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    def test_login(self):
        #定义变量code，调用common的get_code函数，获取注册验证码
        code = get_code('13409958786',2)
        url = host + '/zymn/api/task/login'
        data = {"phone":"13409958786","password":md5('chen1230'),"code":code}
        r = requests.post(url=url,json=data)
        a = '1000'
        b = r.json()["msgcode"]
        self.assertEqual(a,b)

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()