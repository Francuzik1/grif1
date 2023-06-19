import psycopg2
import Orm
from psycopg2 import OperationalError


class WorkBase:
    single_var = None
    connection = None

    def __new__(cls, *args, **kwargs):
        if cls.single_var is None:
            cls.single_var = super().__new__(cls)
        return cls.single_var

    def __init__(self, d_name, user, password, host, port):
        self.d_name = d_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def create_connection(self):
        try:
            self.connection = psycopg2.connect(
                database=self.d_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as error:
            print(f"The error '{error}' occurred")
        return self.connection

    #def getSelect(self):
        #return new \Orm\Select()

    #def fetchAll(self, select):
        #return self.connection.cursor.execute(select.getSelect())