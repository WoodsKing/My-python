import random
# 随机random模块
"""
seed()                          初始化随机种子
random()                        生成[0.0,1.0)只见随机数
ranint(a,b)                     生成[a,b]之间的整数
getrandbits(k)                  生成k比特长的随机数
randregan(star,stop[,stsp])     生成一个[star,stop)之间step为步数的随机整数
uniform(a,b)                    生成[a,b]间随机小数
choice(sep)                     从序列类型sep，随机返回元素
shuffle(sep)                    将序列随机排列，返回打乱后的序列
sample(pop,k)                   从pop类型中随机选取k个元素返回
"""

list1 = 'qwertyuiop'
print(random.sample(list1,5))