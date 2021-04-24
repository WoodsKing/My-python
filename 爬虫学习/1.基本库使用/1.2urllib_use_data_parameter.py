import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word': 'hello', 'user': 'My'}), encoding='utf-8')
response = urllib.request.urlopen('https://httpbin.org/post', data=data)  # 传输的data参数在form字段中显示
print(response.read())
