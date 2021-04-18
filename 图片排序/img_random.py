import os
import random

# 产生随机数


def random_name():
    a = "1234567890qwertyuiopasdfghjklzxcvbnm"
    name = random.choice(a)
    for i in range(5):
        name = name + random.choice(a)
    return name
# 主函数


def main():
    
    list_jpg_buff = os.popen("dir *.jpg /b")
    list_jpg = list_jpg_buff.readlines()
    print(list_jpg)
    for i in list_jpg:
        name1 = i[:-1]
        print(name1)
        name = random_name()
        print(name)
        cmd = 'move ' + name1 + ' ' + name + '.jpg'
        os.popen(cmd)


main()
