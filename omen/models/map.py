'''Module consist map for Omen'''

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import peewee as pw

from header import *

'''
Declaration of common variable:
    coordinate: coordinate of objects
    database: variable of meta classes
'''

class BaseModel(pw.Model):
    ''' Base class for all models'''
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database =  pw.SqliteDatabase(MAP_DB)

class Npcs(BaseModel):
    '''class represents npcs'''
    coordinate = pw.TextField()


class Players(BaseModel):
    '''class represents players'''
    coordinate = pw.TextField()

class Things(BaseModel):
    '''class represents things'''
    coordinate = pw.TextField()


class MapObj(BaseModel):
    ''' class represent object on map '''
    coordinate = pw.TextField()
    json_obj = pw.TextField()


class Etc(BaseModel):
    '''class represents etc'''
    coordinate = pw.TextField()


map_db = pw.SqliteDatabase(MAP_DB)
map_db.create_tables([Npcs, Players, Things, MapObj, Etc])
