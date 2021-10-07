import json
import os

class BD():
    def __init__(self):
        self.cwd = os.getcwd()

    def open_in_read_mode(self):
        arquivo = open(f'{self.cwd}\\src\\bd\\bd.json', 'r')
        db_json = json.loads(arquivo.read())
        arquivo.close()
        return db_json
    
    def insert_in_BD(self, objeto):
        try:
            bd_json_list = self.open_in_read_mode()
            bd_json_list.append(objeto)
            print(bd_json_list)
            arquivo = open(f'{self.cwd}\\src\\bd\\bd.json', 'w')
            arquivo.write(json.dumps(bd_json_list))
            arquivo.close()
            return True
        except:
            return False

bd = BD()