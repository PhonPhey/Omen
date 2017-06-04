'''Init module'''

from omen.header import *
from omen.data_db import *
from peewee import  *

def init_db():
    '''Function for inital db if it not inited'''
    db  = SqliteDatabase("Omen/omen/"+DATA_DB)
    db.create_tables([Players, Inventory, Events, Things, Monsters, Npcs])
    
    
    