import requests

headers = {
    'cookie': '_zap=3255b39c-4465-4ee6-8305-7f8c439d52a0; _xsrf=YEdHGMV0ZuJ5alfy9iVVwAch8Qaodzus; '
              'd_c0="ANCfGC1g6BKPTpnBazH4LLpURjDU7ivXcp8=|1617612113"; '
              'captcha_session_v2="2|1:0|10:1617612115|18:captcha_session_v2|88'
              ':VUVLcE1VdGRZdnNvUlAzc2VibDQwTS9ZYkl6d3pLVEtVRlJOTnFzTGdVUmNkOVFwVjNwbW45NEc4dEZHK3Zvaw'
              '==|5ca4554674d01d816839478c4a047a0725b15f81c5cf738eeaa45ebb98ad886f"; __snaker__id=oDoGSyE4Xjx1gEdW; '
              'gdxidpyhxdE=8igZZ3qlZiLIy8goUp7wBVCtt5DMICt1l1ni4RGLPjtodMNh9rr9zlSxSQYbcTlfIcMdCJs91awcq3tNYGcX1zA'
              '%2Bvb%5C8TGEv52jqr%2F%5CHyt9YXZN%5CBbEtU3SUKxsbnDiwjoL%2BQO'
              '%2BuD2tyxY0Ec5q6uZsiirp6Cz6bTj4ZKq5ssnKcjCov%3A1617613015287; _9755xjdesxxd_=32; '
              'YD00517437729195%3AWM_NI=zcvipIQh%2FWPmjG6cIKWHmEBoNEnrn2hUptlbKw%2B3bicBd5%2F38Z7MulUmM7J%2BDCR'
              '%2Fh2jcbtlJiAjF0xnMLSLtdYf9%2FGaiZ2MvjtR8ceSIlXTXJuhmYZyopCK9llArNP2lTXk%3D; '
              'YD00517437729195%3AWM_NIKE'
              '=9ca17ae2e6ffcda170e2e6eed3d26e8993fe95d969bbbc8bb7c85a968a8aaaaa688fa89da8f63c9c9184a7c82af0fea7c3b92ababdba8af34393b8e1b8d367aa99fa84cc419598a3a6c1658e9ba293ed3aac8bc095ef6a89a9e5d4e163a19eacd6ae39fc86f9aef86897b383d8c921889d9ed0eb3aaabdae95ef42ab9fa6a7b374ae9384b4cf80a887aadaae4da3b796d3d07eaaac9ed9e26f9197a4b9d7548aaba88edc52bbb1c0a4ca33b0b48f93cd5cf2b49cb9ea37e2a3; YD00517437729195%3AWM_TID=FG9eUguy3tdBEUEVQAJqkNhSXgkDLbUR; z_c0="2|1:0|10:1617612394|4:z_c0|92:Mi4xU0tmTUZnQUFBQUFBMEo4WUxXRG9FaWNBQUFDRUFsVk5hVnVTWUFCaDhpSjNEVE1Zelg3U2VVZmVIeU5NaU5iSG5B|84292b1f90bb7e9db8673d05ae60053ce4e5b05dba0d39c47a29ef41f60f1016"; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1618834183,1618844576,1619249529,1619315152; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1619315152; SESSIONID=Tqq8rwkp6VSj8CcjvBvyocmybvDqpeNvIDxlRBGEZGD; KLBRSID=fe0fceb358d671fa6cc33898c8c48b48|1619315152|1619315149; JOID=UlkWBEr1n69mrEn7G_CfczaALhMKoOzaWN8_km_CyP4IkguZcyZQKQGsSv0ZoOxabaSxbW35Pa2xjb13Hlwc2g8=; osd=V1sWAEnwna9ir0z5G_ScdjSAKhAPouzeW9o9kmvBzfwIlgiccSZUKgSuSvkape5aaae0b239Pqizjbl0G14c3gw=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.128 Safari/537.36 '
}
r = requests.get(r'https://www.zhihu.com/', headers=headers)
print(r.text)