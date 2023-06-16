import psycopg2
from psycopg2 import OperationalError


class WorkBase:
    fof = None

    def __new__(cls, *args, **kwargs):
        if cls.fof is None:
            cls.fof = super().__new__(cls)
        return cls.fof

    def __init__(self, d_name, user, password, host, port):
        self.d_name = d_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(
                database=self.d_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection


Test1 = WorkBase("horse", "postgres", "1111", "127.0.0.1", "5432")
h = Test1.create_connection()
cur = h.cursor()
cur.execute("select * from products;")
result = cur.fetchall()
print(result)

