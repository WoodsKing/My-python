# 首先导入PyMySQL库
import pymysql
import datetime, time

# 连接数据库，创建连接对象connection
# 连接对象作用是：连接数据库、发送数据库信息、处理回滚操作（查询中断时，数据库回到最初状态）、创建新的光标对象
connection = pymysql.connect(host='localhost',  # host属性
                             user='root',  # 用户名
                             password='123456',  # 此处填登录数据库的密码
                             db='managetask',  # 数据库名
                             )
cursor = connection.cursor()
create_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(create_time)
sql="insert into taskrecord(taskname,date) values(\'%s\',\'%s\');"%('记单词1',create_time)
print(sql)
rows = cursor.execute(sql)
print(rows)
connection.commit()
cursor.close()
connection.close()
