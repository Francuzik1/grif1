from WorkBase import WorkBase
from Config import Config
from Orm.Selector import Selector
Selector().where(["id = 4"])
Selector().selectfield("password")
request: str = Selector().searcher()
Test1 = WorkBase(Config().dbs_name(), Config().dbs_user(), Config().dbs_password(), Config().dbs_host(), Config().dbs_port())
Base = Test1.create_connection()
print(request)
cur = Base.cursor()
cur.execute(request)
result = cur.fetchall()
print(result)


# не из бд, а из ввода пользователя
# в бд будет таблица с одной колонкой - числа
# доствть из бд все числа, собрать односвязный (потом двусвязный список), возможность добавления/удаления и сортировки списка
# достать из бд все числа и построить b-дерево. добавить возможность добавления/удаления метода и балансировки дерева
# --//-- rd-tree
