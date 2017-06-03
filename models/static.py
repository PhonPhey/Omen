'''Module consist static for Omen'''

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import peewee as pw

from header import *

'''
Declaration of common variable:
    name: name of object of [class_object]
    json_meta_obj: json object of meta class
    database: variable of meta classes
'''

class BaseModel(pw.Model):
    ''' Base class for all models'''
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database =  pw.SqliteDatabase(STATIC_DB)

class Things(BaseModel):
    '''class represents things'''
    name = pw.TextField()
    json_meta_obj =  pw.TextField()

class Monsters(BaseModel):
    '''class represents monsters'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

class Npcs(BaseModel):
    '''class represents npcs'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

class Events(BaseModel):
    '''class represents events'''
    name = pw.TextField()
    json_obj = pw.TextField()

static_db = pw.SqliteDatabase(STATIC_DB)
static_db.create_tables([Things, Monsters, Npcs, Events])