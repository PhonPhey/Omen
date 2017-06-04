"""Module consist data for Omen"""

import peewee as pw

from omen.header import *

'''
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
    coordinate: coordinate of objects
    name: name of object of [class_object]
'''


class BaseModel(pw.Model):
    ''' Base class for all models'''
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database =  pw.SqliteDatabase(DATA_DB)

class Players(BaseModel):
    coordinate = pw.TextField()
    name = pw.TextField()

class Inventory(BaseModel):
    player_id = pw.PrimaryKeyField(unique=True)

class Events(BaseModel):
    name = pw.TextField()
    json_event_obj  =  pw.TextField()

class Things(BaseModel):
    name = pw.TextField()
    coordinate = coordinate = pw.TextField()
    
class Monsters(BaseModel):
    name = pw.TextField()
    coordinate = pw.TextField()

class Npcs(BaseModel):
    name = pw.TextField()
    coordinate = pw.TextField()