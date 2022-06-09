import requests
import pymysql
import hashlib

#定义变量contract，是请求协议
contract = 'http://'
#定义变量ip,是服务器的ip
ip = '192.168.10.249'
#定义变量port,是端口
port = ':1234'
#定义host
host = contract + ip + port

#定义获取验证码的函数
def get_code(phone,type):
    url = 'http://192.168.10.249:1234/zymn/api/task/GetVcode'
    data = {"phone":phone,"type":type}
    r = requests.post(url=url,data=data)
    return r.json()["phoncode"][0]

#定义md5加密的函数
def md5(str):
    m = hashlib.md5()
    m.update(str.encode(encoding='utf-8'))
    return m.hexdigest()

#定义获取token的函数
def get_token(phone,passwd):
    code = get_code(phone,2)
    url=host + '/zymn/api/task/login'
    data = {"phone":phone,"password":md5(passwd),"code":code}
    r = requests.post(url=url,json=data)
    return r.json()["userInfo"][0]["token"]



def execute_sql(sql):
    db = pymysql.connect('192.168.10.249','admin','123456','zymn')
    #定义变量cr，获取游标
    cr = db.cursor()
    #执行sql语句
    cr.execute(sql)
    #提交事务
    db.commit()
    #关闭数据库连接
    db.close()
    #关闭游标
    cr.close()