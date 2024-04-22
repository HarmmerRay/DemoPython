# 从java程序中得到json数据 -->解析数据生成响应的sql，python中执行这些sql
# {"databaseName":"studentInfo",
# "tableInfo":{
#   "tableName":xxx,
#   "columnNames":"uid uname upassword uphone umail"
# }
# }
import sqlite3

# 连接到数据库（如果不存在，将创建一个新的数据库文件）
conn = sqlite3.connect('example.db')

# 创建一个游标对象
c = conn.cursor()

# 创建一个新表
c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# 提交更改
conn.commit()

# 关闭连接
conn.close()