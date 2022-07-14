import unittest
from public.common import *


class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    def test_upload(self):
        url = host + '/zymn/api/task/AddPic'
        #定义head是请求头信息，调用common模块get_token函数去获取token
        head = {"token":get_token('13409958786','chen1230')}
        file = {"image":open(r'贴吧接口自动化\1.jpg','rb')}
        r = requests.post(url=url,headers=head,files=file)
        a = '1000'
        b = r.json()["msgcode"]
        self.assertEqual(a,b)

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()