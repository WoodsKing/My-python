import requests
import time
xuehao = '1903021709'   #学号
mima = 'xtt988520'  #密码


class Signin_Cqcet:

    def __init__(self, username, password,weekl):

        self.sign_data = {
    'type':1,
    'username': username,
    'password': password,
    'rememenber': 'on',
    'img_code':'',
}
        self.list_data = {
    'pageSize':'10',
    'pageNum':'1',
    'isAsc':'asc',
    'xnxq':'2020-2021-2',
    'weekly':weekl
}
        self.session = requests.Session()
        self.login_url = 'http://sso.cqcet.edu.cn/login'
        self.login_process_url = 'http://sso.cqcet.edu.cn/uaa/login_process'
        self.evaluation_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/index/teach'
        self.get_list_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/xskb/list'
        self.add_url = 'http://ossc.cqcet.edu.cn/xg/teaching/student/teach/add'
    #登入智慧校园
    def Signin(self):
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/89.0.4389.128 Safari/537.36 ',
            'Host': 'ossc.cqcet.edu.cn'
        }
        self.session.headers.update(headers)
        self.session.get(self.login_url)
        time.sleep(0.1)
        r = self.session.post(self.login_process_url,data=self.sign_data)
        time.sleep(0.1)
        print(r.request.headers)

    # 获取教评信息
    def getlist(self):
        self.Signin()
        self.session.get(self.evaluation_url)
        time.sleep(0.1)
        list = self.session.post(self.get_list_url,data=self.list_data)
        print(list.request.headers)
        time.sleep(0.1)
        return list.json()['rows']

    #开始教评
    def post_add(self):
        add_data_list =  self.getlist()
        add_data = {
            'evaluationProject': [{"name":"老师教得怎么样?","id":"teach_situation","value":"5"},
                {"name":"学习收获怎么样?","id":"learn_harvest","value":"5"},
                {"name":"纪律管理怎么样?","id":"discipline","value":"5"},
                {"name":"课堂互动怎么样?","id":"interaction","value":"5"},
                {"name":"课后交流怎么样?","id":"communicat","value":"5"}],
            'remark':'',
            'advice':'',
            'kkdm':''
        }
        for i in add_data_list:
            add_data['xh'] = i['xh']
            add_data['xm'] = i['xm']
            add_data['skjsjgh'] = i['skjsjgh']
            add_data['skjsmc'] = i['skjsmc']
            add_data['year'] = i['xn']
            add_data['term'] = i['xq']
            add_data['taskId'] = i['yxh']
            add_data['weekly'] = i['weekly']
            r = self.session.post(self.add_url,data=add_data)
            print(r.request.headers)
"""
            print(add_data)
            print(r.text)
            time.sleep(0.1)
            print(i['complete'])
            print('已教评：',i['kcmc'])
"""



cqcet = Signin_Cqcet(xuehao,mima,7)
cqcet.Signin()
cqcet.post_add()
