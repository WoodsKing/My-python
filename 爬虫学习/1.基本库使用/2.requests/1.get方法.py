import requests

data = {
    'name': 'germey',
    'age': 22
}
r = requests.get('http://httpbin.org/get?name=germey&age=22')
b = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(b.text)