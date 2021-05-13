import requests
import random
import time


def random_31():
    a = ''
    str_list = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(32):
        str_1 = str_list[random.randint(0, 61)]
        a += str_1
    return a


random_code = random_31()
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ??? Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 MMWEBID/9686 MicroMessenger/7.0.22.1820('
                  '0x27001636) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 '
}

url = 'http://weixin.cqcet.edu.cn/smallwx/portal/new/?code=' + random_code + '&state=123'
session = requests.Session()
session.headers.update(header)
r = session.get(url)
r.encoding = 'utf-8'
print(r.url)
print(r.status_code)
# print(r.text)

timestamp = str(int(round(time.time() * 1000)))
url1 = 'http://ossc.cqcet.edu.cn/exposed/token/getToken?userId=1903021662&timeStamp=' + timestamp
r = session.get(url1)
r.encoding = 'utf-8'
print(r.url)
print(r.status_code)
token = r.json()['data']

url2 = 'http://ossc.cqcet.edu.cn/exposed/v1/Sys/1903021662?token_k=1903021662_' + timestamp + '&token_v=' + token + '&platform=2'
print(url2)
r = session.get(url2)
r.encoding = 'utf-8'
print(r.url)
print(r.status_code)
print(r.text)

url3 = 'http://ossc.cqcet.edu.cn/openapi/api-auth/oauth/client/token'
headers1 = {
    'Referer': url
}
r = session.options(url3,headers=headers1)
r.encoding = 'utf-8'
print(r.url)
# print(r.request.headers)
print(r.status_code)
print(r.text)

json = {
    'code': random_code
}
r = session.post(url3, headers=headers1,json=json)
r.encoding = 'utf-8'
print(r.url)
# print(r.request.headers)
print(r.status_code)
print(r.text)