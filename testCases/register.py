import unittest
from public.common import *


class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    def test_reg(self):
        #定义变量code，调用common的get_code函数，获取注册验证码
        code = get_code('13409958700',1)
        url = host + '/zymn/api/task/reg'
        data = {"phone":"13409958700","password":"chen1230","code":code}
        r = requests.post(url=url,data=data)
        a = '1000'
        b = r.json()["msgcode"]
        self.assertEqual(a,b)

    def tearDown(self):
        #调用common的execute_sql函数，删除账号数据
        execute_sql('delete from reg where phone="13409958700"')



if __name__ == '__main__':
    unittest.main()