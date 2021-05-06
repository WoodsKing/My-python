# conding=utf-8
import requests
import json
mm = [{"name": "老师教得怎么样?", "id": "teach_situation", "value": "5"},
                          {"name": "学习收获怎么样?", "id": "learn_harvest", "value": "5"},
                          {"name": "纪律管理怎么样?", "id": "discipline", "value": "5"},
                          {"name": "课堂互动怎么样?", "id": "interaction", "value": "5"},
                          {"name": "课后交流怎么样?", "id": "communicat", "value": "5"}]
data = {
    'evaluationProject': json.dumps(mm),
    'kk': '喃喃'
}
json = {
    'evaluationProject': mm
}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)