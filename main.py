from Class_WorkBase import WorkBase
from Class_Config import Config


limit = (Config().reader())
Test1 = WorkBase("horse", "postgres", "1111", "127.0.0.1", "5432")
Base = Test1.create_connection()
cur = Base.cursor()
if limit == "":
    cur.execute("select * from products;")
else:
    cur.execute("select * from products where " + limit + ";")
result = cur.fetchall()
print(result)
