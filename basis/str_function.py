"""

字符串表示3种方法
1:''                        ’表示可使用”作为字符串的一部分
2:""                        "表示可使用'作为字符串的一部分
3:''' '''                   '''表示可使用‘ “ 也可以换行


"""

str1 = 'qwertyuiop'
print(str1[:-1])            # 切片
print(str1[1:])             # 切片
print(str1[1:-1])           # 切片

str2 = 2 * str1             # 复杂
print(str2)

print(str1 + str1)          # 连接

print('q' in str1)          # 判断包含
