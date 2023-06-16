import json


class Config:

    def __init__(self):
        filename = "config.json"
        with open(filename, 'r') as info:
            limitation = json.load(info)
        self.var_limit = limitation

    def reader(self):
        return self.var_limit
