import requests
import time

username = '1903021662'  # 学号
password = '2465681755mjy'  # 密码
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 ',
    'Host': 'ossc.cqcet.edu.cn'
}
data = {
    'type': 1,
    'username': username,
    'password': password,
    'rememenber': 'on',
    'img_code': '',
}
s = requests.Session()
s.get('http://sso.cqcet.edu.cn/login', headers=headers)
time.sleep(0.1)
r = s.post('http://sso.cqcet.edu.cn/uaa/login_process', data=data)
time.sleep(0.1)
print(r.request.headers)
