from pymysql import Connection

conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='000000',
    autocommit=True
)
print(conn.get_server_info())

cursor = conn.cursor()
conn.select_db("test")
cursor.execute("select * from student")
results: tuple = cursor.fetchall()
for r in results:
    print(r)
conn.close()
