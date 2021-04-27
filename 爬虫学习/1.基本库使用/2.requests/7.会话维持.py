import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/ste/unber/12345678')
r = s.get('http://httpbin.org/cookies')
print(r.text)