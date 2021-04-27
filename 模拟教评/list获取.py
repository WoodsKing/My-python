import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 ',
    'Cookie': 'JSESSIONID=c661d0d6-9dcd-41ff-8080-55e685e87032; JSESSIONID=0B324F4B7CE8E29E3FCB09A76F018A13; login_name=1903021662',
    'Host': 'ossc.cqcet.edu.cn'
}
data1 = {
    'pageSize':'10',
    'pageNum':'1',
    'isAsc':'asc',
    'xnxq':'2020-2021-2',
    'weekly':'8'
}
r = requests.post('http://ossc.cqcet.edu.cn/xg/teaching/student/xskb/list',data=data,headers=headers)
for key,value in r.json().items():
    print(key,'=',value)