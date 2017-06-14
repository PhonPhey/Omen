'''Util module for Omen Engine'''

import hashlib

from jsonsempai import magic
from Omen.locale import ru_RU as locale

from Omen import data_db

from Omen import header as h

from peewee import  *

from termcolor import colored

def valid_point(record, max_point, min_point):
    if record < min_point:
        print(colored(locale.error, 'red') + ": " + str(record) + " < " + str(min_point))
        exit(1)
    elif record > max_point:
        print(colored(locale.error, 'red') + ": " +  str(record) + " > " + str(max_point))
        exit(1)
    return record


def init_db():
    """Function for inital db if it not inited"""
    
    db  = SqliteDatabase(h.PATH_DB)
    db.create_tables([data_db.Player, data_db.Inventory, data_db.Event, data_db.Thing, data_db.Monster, data_db.NPC, data_db.Other])
    
    
def in_quot(str):
        return "\"" + str + "\""
    