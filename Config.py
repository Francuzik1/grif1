import json


class Config:

    def __init__(self):
        filename = "config.json"
        with open(filename, 'r') as info:
            limitation = json.load(info)
            self.db_name = limitation.get("database")
            self.db_user = limitation.get("user")
            self.db_password = limitation.get("password")
            self.db_host = limitation.get("host")
            self.db_port = limitation.get("port")

    def dbs_name(self):
        return self.db_name

    def dbs_user(self):
        return self.db_user

    def dbs_password(self):
        return self.db_password

    def dbs_host(self):
        return self.db_host

    def dbs_port(self):
        return self.db_port
