from Class_WorkBase import WorkBase
from Class_Config import Config

wh = "manufacturer = 'Apple'"
Test1 = WorkBase(Config().dbs_name(), Config().dbs_user(), Config().dbs_password(), Config().dbs_host(), Config().dbs_port())
Base = Test1.create_connection()
cur = Base.cursor()
if wh == "":
    cur.execute("select * from products;")
else:
    cur.execute("select * from products where " + wh + ";")
result = cur.fetchall()
print(result)
