import os
import re


# 获取文件列表


def get_list():
    a = []
    d = os.popen("dir *.jpg /b")
    x = d.readlines()
    for i in x:
        a.append(i[:-5])
    return a


# 列表分类


def serch_str(str_list):
    unber_list = []
    char_list = []
    for i in str_list:
        if re.match('[0-9]+$', i):
            unber_list.append(i)
        else:
            char_list.append(i)
    return unber_list, char_list


def move_name(unber_list, char_list):
    str_len = len(unber_list) + len(char_list)  # 获取总长度
    print('\nunber:%d\nonunber:%d\nsmu%d\n' % (len(unber_list), len(char_list), len(unber_list) + len(char_list)))
    int_unber_list = []
    char_list_flag = 0
    # 将str传化为int
    for i in unber_list:
        j = int(i)
        int_unber_list.append(j)
    # 排序int_unber_list
    int_unber_list.sort()

    for i in range(str_len):
        # print('第一次%d'%(i+1))
        if i + 1 not in int_unber_list:
            # print('第二次%d'%(i+1))
            if int_unber_list:
                if int_unber_list[-1] > str_len:
                    cmd = 'move ' + str(int_unber_list[-1]) + '.jpg ' + str(i + 1) + '.jpg'
                    print(cmd)
                    os.popen(cmd)
                    int_unber_list.pop()
                else:
                    cmd = 'move ' + char_list[char_list_flag] + '.jpg ' + str(i + 1) + '.jpg'
                    print(cmd)
                    os.popen(cmd)
                    char_list_flag += 1
            else:
                cmd = 'move ' + char_list[char_list_flag] + '.jpg ' + str(i + 1) + '.jpg'
                print(cmd)
                os.popen(cmd)
                char_list_flag += 1


def main():
    str_list = get_list()  # 获取文件夹下文件
    print(str_list)  # show list
    str_len = len(str_list)  # 列表总长度

    print('\n文件总数:%d ' % str_len)  # 显示文件总数
    unber_list, char_list = serch_str(str_list)  # 获取 数字文件与非数字文件
    print('\n纯数字：\n%s \n非纯数字：\n %s\n' % (unber_list, char_list))  # 显示
    move_name(unber_list, char_list)


main()
