import requests
import random
import time

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ??? Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 MMWEBID/9686 MicroMessenger/7.0.22.1820('
                  '0x27001636) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 '
}
session = requests.Session()
session.headers.update(header)


def random_code(un):
    a = ''
    str_list = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    for i in range(un):
        str_1 = str_list[random.randint(0, 61)]
        a += str_1
    return a


random_code = random_code(32)


def code_state():
    url = 'http://weixin.cqcet.edu.cn/smallwx/portal/new/?code={}&state=123'.format(random_code)
    r = session.get(url)
    time.sleep(0.1)
    print(r.status_code)


def get_openid():
    url = 'http://weixin.cqcet.edu.cn/wxmp/wxUserInfo/getUserInfo_new1?token_k=200320030_undefined&token_v=&code={}'.format(random_code)
    print(url)
    r = session.get(url)
    time.sleep(0.1)
    print(r.status_code)
    print(r.json())


def author():
    appid = 'wx8e0d3615ca25d473'
    uri = 'http://ossc.cqcet.edu.cn/exposed'
    times = str(int(round(time.time() * 1000)))
    url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid={}&redirect_uri={}&response_type=code&scope=snsapi_base&state=123#wechat_redirect'.format(appid, uri,)
    print(url)
    r = session.get(url)
    print(r.text)


# author()
code_state()
get_openid()

