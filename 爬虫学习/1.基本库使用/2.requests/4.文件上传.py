import requests

files = {'file': open('favicon.ico', 'rb')}
b = requests.post('http://httpbin.org/post', files=files)   # 文件上传
print(b.text)