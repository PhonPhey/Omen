'''Init module'''

import hashlib

from omen.header import *
from omen.models.data_db import *
from peewee import  *

def init_db():
    '''Function for inital db if it not inited'''
    db  = SqliteDatabase(DATA_DB)
    db.create_tables([Players, Inventory, Events, Things, Monsters, Npcs, Etc])
    
    
def _check_db():
    if SHA512_DB != "":
        hash_md5 = hashlib.md5()
        with open(DATA_DB, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
             hash_md5.update(chunk)
            
        print(hash_md5.hexdigest())