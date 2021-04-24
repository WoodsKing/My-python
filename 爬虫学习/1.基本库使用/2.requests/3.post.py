import requests

data = {'name': 'germey', 'age': '22'}

r = requests.post('http://httpbin.org/post', data=data)  # 表单提交
print(r.text)


