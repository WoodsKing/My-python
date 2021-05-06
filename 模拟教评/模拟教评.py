import requests
from urllib.parse import urlencode
import time
import json

xuehao = '1903021662'  # 学号
mima = '2465681755mjy'  # 密码


class signincqcet:

    def __init__(self, username, password, weekl):
        self.sign_data = {
            'type': 1,
            'username': username,
            'password': password,
            'rememenber': 'on',
            'img_code': '',
        }
        self.list_data = {
            'pageSize': '10',
            'pageNum': '1',
            'isAsc': 'asc',
            'xnxq': '2020-2021-2',
            'weekly': weekl
        }
        self.session = requests.Session()
        self.login_url = 'http://sso.cqcet.edu.cn/login'
        self.login_process_url = 'http://sso.cqcet.edu.cn/uaa/login_process'
        self.evaluation_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/index/teach'
        self.get_list_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/xskb/list'
        self.add_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/teach/add'

    # 登入智慧校园
    def signin(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.128 Safari/537.36 ',
            'Host': 'ossc.cqcet.edu.cn'
        }
        self.session.headers.update(headers)
        self.session.get(self.login_url)
        time.sleep(0.1)
        k = self.session.post(self.login_process_url, data=self.sign_data)
        time.sleep(0.1)
        # print(k.request.headers)

    # 获取教评信息
    def getlist(self):
        self.signin()
        self.session.get(self.evaluation_url)
        time.sleep(0.1)
        list = self.session.post(self.get_list_url, data=self.list_data)
        # print(list.request.headers)
        time.sleep(0.1)
        return list.json()['rows']

    # 开始教评
    def post_add(self):
        add_data_list = self.getlist()
        mm = [{"name": "老师教得怎么样?", "id": "teach_situation", "value": "5"},
              {"name": "学习收获怎么样?", "id": "learn_harvest", "value": "5"},
              {"name": "纪律管理怎么样?", "id": "discipline", "value": "5"},
              {"name": "课堂互动怎么样?", "id": "interaction", "value": "5"},
              {"name": "课后交流怎么样?", "id": "communicat", "value": "5"}]
        data = {
            'evaluationProject': json.dumps(mm),
            'xh': '',
            'xm': '',
            'skjsjgh': '',
            'skjsmc': '',
            'year': '',
            'term': 2,
            'weekLy': '',
            'taskId': ''
        }
        for i in add_data_list:
            data['xh'] = i['xh']
            data['xm'] = i['xm']
            data['skjsjgh'] = i['skjsjgh']
            data['skjsmc'] = i['skjsmc']
            data['year'] = i['xn']
            data['term'] = i['xq']
            data['weekLy'] = i['weekly']
            data['taskId'] = i['yxh']
            # print(data)
            if not i['complete']:
                r = self.session.post(self.add_url, data=data)
                time.sleep(0.1)
            print('已教评第{}周：{}'.format(i['weekly'], i['kcmc']))


def main():
    print('*************************')
    print('如果是单周直接输入即可')
    print('如果是多个周此请用,号隔开')
    print('列如：1,2,3')
    print('*************************')
    week_list = input('请输入周此:')
    week = week_list.split(',')
    print(week)
    for i in week:
        print('*******************第{}周*******************'.format(int(i)))
        cqcet = signincqcet(xuehao, mima, int(i))
        cqcet.signin()
        cqcet.post_add()


main()
