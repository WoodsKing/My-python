import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ??? Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 MMWEBID/9686 MicroMessenger/7.0.22.1820('
                  '0x27001636) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 '
}
headers1 = {
    'Referer': 'http://ossc.cqcet.edu.cn/openapi/api-auth/oauth/client/token'
}
s = requests.Session()
s.headers.update(header)
r = s.get('http://httpbin.org/get')
print(r.text)

req = requests.Request('GET', 'http://httpbin.org/get', headers=headers1)
prepped = s.prepare_request(req)
r = s.send(prepped)

print(r.text)