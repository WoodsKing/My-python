import urllib.request

response = urllib.request.urlopen('https://www.python.org')
# print(response.read().decode('utf-8'))              # 网页源码
print('数据类型', type(response))  # 数据类型
print('状态码', response.status)  # 状态码

print('显示请求头',response.getheaders())   # 显示响应头
print('显示请求头server的value', response.getheader('Server'))  # 显示响应头特定值
