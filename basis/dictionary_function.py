# 字典basis
dictionary = {}  # 可创建空字典
dictionary1 = {"中国": "北京", "美国": "华盛顿", "法国": "巴黎"}

print('1.dictionary1["中国"]:\t',dictionary1["中国"])  # 输出为北京
print("2.dictionary1:\t",dictionary1)  # 这个字典

# 增加元素
dictionary1["英国"] = "伦敦"  # dictionary1["键"] = ”值“
"""
函数与方法
keys()                  返回所有建信息
values()                返回所有值信息
items()                 返回所有键值对
get(<key>,<default>)    键存在则返回相应值，否则返回默认
pop(<key>,<default>)    键存在则返回相应值，同时删除键值对，否则返回默认值
popitem()               随机从字典中取出一个键值对，以元组(key,value)形式返回
clear()                 删除所有键值对
del dictionart.<key>    删除字典中某个键值对
<key> in <d>            key是否在字典内
"""
a = dictionary1.keys()
print("3.keys():\t", a)     # 返回类型为’dict_keys‘

a = dictionary1.values()
print("4.values():\t", a)   # 返回类型’dict_values‘

a = dictionary1.items()
print("5.items():\t",a)     # 返回类型'dict_items'

a = dictionary1.get('美国','加拿大')     # 返回类型’str‘
print("6.get('美国','加拿大'):\t",a)
a = dictionary1.get('德国','加拿大')
print("7.get('德国','加拿大'):\t",a)
