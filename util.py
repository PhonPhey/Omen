'''Util module for Omen Engine'''

import hashlib

from Omen import data_db

from Omen import header as h

from peewee import  *

from termcolor import colored

def valid_point(record, max_point, min_point):
    if record < min_point:
        print(colored("Ошибка", 'red') + ": введенное число меньше допустимого значения")
        exit(1)
    elif record > max_point:
        print(colored("Ошибка", 'red') + ": введенное число больше допустимого значения")
        exit(1)
    return record


def init_db():
    """Function for inital db if it not inited"""
    
    db  = SqliteDatabase(h.PATH_DB)
    db.create_tables([data_db.Player, data_db.Inventory, data_db.Event, data_db.Thing, data_db.Monster, data_db.NPC, data_db.Other])
    
    
def check_db():
    """Function for check databse hash sum"""
        
    hash_sha512= hashlib.sha512()
    file_db = open(h.PATH_DB, "rb")
    old_hash = open(h.PATH_FILE_HASH_SUM, "rb").read().decode("utf-8")

    with open(h.PATH_FILE_HASH_SUM, "w") as file_sum:
            
        print("Хеш-сумма из файла: " + old_hash)
            
        for chunk in iter(lambda: file_db.read(4096), b""):
            hash_sha512.update(chunk)
            
        print("Хеш-сумма базы данных: " + hash_sha512.hexdigest())
                
        if old_hash == "":
            file_sum.write(hash_sha512.hexdigest())
        
        elif old_hash != hash_sha512.hexdigest():
            print(colored("Предупреждение", 'yellow') +": хеш-сумма базы данных несовпадает с контрольной суммой, созданной после прошлого выключения. Авто замена")
            file_sum.write(hash_sha512.hexdigest())
               
        else:
            file_sum.write(hash_sha512.hexdigest())
            