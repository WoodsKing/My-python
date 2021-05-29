"""
本程序是一个验证程序起因是因为一个短视频所描述的问题：
有三个箱子，一个有奖两个为空，当自己选了一个过后主持人会打开一个空箱子。之后问你换不换，视频中说的是换的画概率会高些
"""
import random

# 箱子所处状态
Selected = 'Selected'  # 选中
Unselected = 'Unselected'  # 未选中
Display = 'display'  # 显示

prize_pool = ['谢谢惠顾', '奖', '谢谢惠顾']  # 奖池定义
pool_store_information = None
# 箱子定义
box = {
    'box1': [Unselected, pool_store_information],
    'box2': [Unselected, pool_store_information],
    'box3': [Unselected, pool_store_information]
}


# 初始化奖池
def inti_pool():
    box['box1'][1] = prize_pool[0]
    box['box2'][1] = prize_pool[1]
    box['box3'][1] = prize_pool[2]
    box['box1'][0] = Unselected
    box['box2'][0] = Unselected
    box['box3'][0] = Unselected


# 随机奖池生成
def renerate_randomprize():
    random.shuffle(prize_pool)
    box['box1'][1] = prize_pool[0]
    box['box2'][1] = prize_pool[1]
    box['box3'][1] = prize_pool[2]


# 输入箱子选择
def select_box(intdata):
    # print('共有1，2，3个箱子')
    if intdata == '1' or intdata == '2' or intdata == '3':
        box['box' + intdata][0] = Selected
        # print('选中的箱子','box'+intdata)
    else:
        print('输入错误')


# 显示未被选择且没有奖励的箱子
def display_noenbox():
    record_mark = []
    for i in box:
        if box[i][0] == Unselected and box[i][1] == '谢谢惠顾':
            record_mark.append(i)
    if len(record_mark) == 1:
        box[record_mark[0]][0] = Display
        # print('展示的箱子', record_mark[0] + ':' + box[record_mark[0]][1])
    elif len(record_mark) == 2:
        store_random = random.getrandbits(1)
        box[record_mark[store_random]][0] = Display
        # print('展示的箱子', record_mark[store_random] + ':' + box[record_mark[store_random]][1])


# 交换箱子
def exchangebox(indata):
    unselected_buff = None
    selected_buff = None
    if indata == 'yes':
        for i in box:
            if box[i][0] == Unselected:
                unselected_buff = i
            if box[i][0] == Selected:
                selected_buff = i
        box[unselected_buff][0] = Selected
        box[selected_buff][0] = Unselected


# 打开选中的箱子并储存中将情况
def open_selectbox():
    open_status = None
    for i in box:
        if box[i][0] == Selected:
            open_status = box[i][1]
            # print('开奖结果：', i+':'+ open_status)
    return open_status


def main():
    totle = 100000
    inti_pool()  # 初始化奖池
    cont = 0
    for i in range(totle):
        inti_pool()  # 初始化奖池
        renerate_randomprize()  # 随机奖池生成
        select_box(str(random.randint(1, 3)))  # 箱子选择
        display_noenbox()  # 显示未被选择且没有奖励的箱子
        exchangebox('yes')  # 交换箱子
        if '奖' == open_selectbox():  # 打开选中的箱子并储存中将情况
            cont += 1
    print('交换箱子的概率：{:.2f}%'.format(cont / totle * 100))

    cont = 0
    for i in range(totle):
        inti_pool()  # 初始化奖池
        renerate_randomprize()  # 随机奖池生成
        select_box(str(random.randint(1, 3)))  # 箱子选择
        display_noenbox()  # 显示未被选择且没有奖励的箱子
        exchangebox('no')  # 交换箱子
        if '奖' == open_selectbox():  # 打开选中的箱子并储存中将情况
            cont += 1
    print('不交换箱子的概率：{:.2f}%'.format(cont / totle * 100))


main()
