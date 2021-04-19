# eval()函数能对字符串进行数值计算

x = 2
y = 3
print(eval('1 + 2'))
print(eval('9 + x'))
print(eval('x + y'))

# eval()可以去掉引号
hello = [1, 34, 5]
str1 = "'hello'"
str2 = 'hello'
print(eval(str1))  # 显示为’hello‘
print(eval(str2))  # 显示为[1,34,5] ,解析过后会将hello当作变量,如果没有定义过hello则会报错
