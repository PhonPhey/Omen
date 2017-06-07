'''Init module'''

import hashlib

from omen import header as h
from omen import shell
from omen import models

from peewee import  *


def _init_db():
    '''Function for inital db if it not inited'''
    
    db  = SqliteDatabase(h.DATA_DB)
    db.create_tables([Players, Inventory, Events, Things, Monsters, Npcs, Etc])
    
    
def _check_db():
        '''Function for check databse hash sum'''
        
        hash_sha512= hashlib.sha512()
        file_db = open(h.DATA_DB, "rb")
        
        with open(HASH_SUM_PATH, "w+") as file_sum:
            if file_sum.read(1) == "":
                for chunk in iter(lambda: file_db.read(4096), b""):
                    hash_sha512.update(chunk)
                file_sum.write(hash_sha512.hexdigest())
            
        print("Check sha512 sum: ", hash_sha512.hexdigest())