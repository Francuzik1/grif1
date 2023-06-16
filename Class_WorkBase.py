import psycopg2
from psycopg2 import OperationalError


class WorkBase:
    single_var = None

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
        except OperationalError as error:
            print(f"The error '{error}' occurred")
        return connection
