import requests

url = 'http://weixin.cqcet.edu.cn/smallwx/portal/new/?code=031u1k0w3kl3lW2q1R0w3UC6VE0u1k0Y&state=123'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ??? Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 MMWEBID/9686 MicroMessenger/7.0.22.1820('
                  '0x27001636) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 '
}

session = requests.Session()
session.headers.update(header)
r = session.get(url)
print(r.history)
print(r.status_code)
print(r.text)