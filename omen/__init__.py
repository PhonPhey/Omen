'''Init module'''

from omen.header import *
from omen.models.data_db import *
from peewee import  *

def init_db():
    '''Function for inital db if it not inited'''
    db  = SqliteDatabase(DATA_DB)
    db.create_tables([Players, Inventory, Events, Things, Monsters, Npcs])
    
    
    