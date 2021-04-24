import requests

headers = {
    'Cookie': 'Hm_lvt_deeb6849ac84929e8ae01644f8d27145=1618734650,1619261777; '
              'Hm_lpvt_deeb6849ac84929e8ae01644f8d27145=1619261777',
    'Host': 'www.cqooc.net/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 '
}
r = requests.get(r'http://www.cqooc.net/', headers=headers)
print(r.text)