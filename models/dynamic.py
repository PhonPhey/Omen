'''Module consist dynamic for Omen'''

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import peewee as pw

from header import *

'''
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
'''


class BaseModel(pw.Model):
    ''' Base class for all models'''
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database =  pw.SqliteDatabase(DYNAMIC_DB)

class Players(BaseModel):
    '''class represents players'''
    name = pw.TextField()


class Inventory(BaseModel):
    '''class represents inventory'''
    player_id = pw.PrimaryKeyField(unique=True, primary_key=True)


class LocalEvents(BaseModel):
    '''class represents local_events'''
    json_event_obj = pw.TextField()


class GlobalEvents(BaseModel):
    '''class represents global_events'''
    json_event_obj = pw.TextField()


dynamic_db = pw.SqliteDatabase(DYNAMIC_DB)
dynamic_db.create_tables([Players, Inventory, LocalEvents, GlobalEvents])