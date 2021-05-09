import time
import requests


url = 'http://ossc.cqcet.edu.cn/exposed/token/getToken?'
header = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; ??? Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36 MMWEBID/9686 MicroMessenger/7.0.22.1820('
                  '0x27001636) Process/tools WeChat/arm32 Weixin NetType/WIFI Language/zh_CN ABI/arm32 '
}
timestamp = str(int(round(time.time() * 1000)))
uersid = '1903021662'
params = {
    'userId': uersid,
    'timeStamp': timestamp
}

session = requests.Session()
session.headers.update(header)
r = session.get(url, params=params)
print(r.history)
print(r.status_code)
print(r.text)