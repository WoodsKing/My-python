import os
import re

# 文件类型声明
filetype_list = ['*.jpg', '*.png']
# filetype_list = ['*.png', '*.jpg']


# 获取文件列表
def get_list(filetype):
    extension_len = len(filetype)
    buff = []
    cmd = 'dir /b ' + filetype
    d = os.popen(cmd)
    x = d.readlines()
    for i in x:
        buff.append(i[:-extension_len])
    return buff


# 列表分类  str_list:文件列表   返回类型[[],[]]二元列表第一个表示数字，第二个表示字符
def serch_str(str_list):
    filelist = []  # 已分类的列表
    unber_list = []  # 数字列表
    char_list = []  # 字符列表
    # 列表筛选
    for i in str_list:
        if re.match('[0-9]+$', i):
            unber_list.append(i)
        else:
            char_list.append(i)
    # 列表合并
    filelist.append(unber_list)
    filelist.append(char_list)
    return filelist


def move_name(unber_list, char_list, filetype):
    str_len = len(unber_list) + len(char_list)  # 获取总长度
    int_unber_list = []
    char_list_flag = 0
    # 将str传化为int
    if unber_list:
        for i in unber_list:
            j = int(i)
            int_unber_list.append(j)
        # 排序int_unber_list
        int_unber_list.sort()

    for i in range(str_len):
        if i + 1 not in int_unber_list:
            if int_unber_list:
                if int_unber_list[-1] > str_len:
                    cmd = 'move ' + str(int_unber_list[-1]) + filetype[1:] + ' ' + str(i + 1 ) + filetype[1:]
                    # print(cmd)
                    os.popen(cmd)
                    int_unber_list.pop()
                else:
                    cmd = 'move ' + char_list[char_list_flag] + filetype[1:] + ' ' + str(i + 1) + filetype[1:]
                    # print(cmd)
                    os.popen(cmd)
                    char_list_flag += 1
            else:
                cmd = 'move ' + char_list[char_list_flag] + filetype[1:] + ' ' + str(i + 1) + filetype[1:]
                # print(cmd)
                os.popen(cmd)
                char_list_flag += 1


# 图片偏移
def offset_img_name(unber_list, offset, filetype):
    count = 1
    int_unber_list = []
    if unber_list:
        for i in unber_list:
            j = int(i)
            int_unber_list.append(j)
        # 排序int_unber_list
        int_unber_list.sort()
    while int_unber_list:
        delmax = int_unber_list.pop()
        cmd = 'move ' + str(delmax) + filetype[1:] + ' ' + str(offset + delmax) + filetype[1:]
        print(cmd)
        os.popen(cmd)


def main():
    offset = 0
    for i in filetype_list:
        filelist = serch_str(get_list(i))
        move_name(filelist[0], filelist[1], i)
    for i in filetype_list:
        filelist = serch_str(get_list(i))
        offset_img_name(filelist[0], offset, i)
        offset = len(filelist[1]) + len(filelist[0])


main()
