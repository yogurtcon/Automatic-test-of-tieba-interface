import unittest
import requests
from public.common import *

class Mytest(unittest.TestCase):

    def setUp(self):
        pass

    def test_reg(self):
        url = host + '/zymn/api/task/GetVcode'
        data = {"phone":"13409958788","type":"1"}
        r = requests.post(url=url,data=data)
        a = "1000"
        b = r.json()["msgcode"]
        self.assertEqual(a,b)


    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()
