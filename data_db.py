"""Module consist models for database for Omen"""

import peewee as pw

from Omen.header import *

"""
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
    coordinate: coordinate of objects
    name: name of object of [class_object]
"""


class BaseModel(pw.Model):
    """Base class for all models"""
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database =  pw.SqliteDatabase(PATH_DATA_DB)

class Player(BaseModel):
    """Class represents players"""
    coordinate = pw.TextField()
    name = pw.TextField()

class Inventory(BaseModel):
    """Class represents inventory"""
    player_id = pw.ForeignKeyField(Player, unique=True)

class Event(BaseModel):
    """Class represents events"""
    name = pw.TextField()
    json_event_obj  =  pw.TextField()

class Other(BaseModel):
    """Class represents races, classes and other"""
    name = pw.TextField()
    type = pw.TextField()
    
class Thing(BaseModel):
    """Class represents things"""
    name = pw.TextField()
    coordinate = pw.TextField()
    
class Monster(BaseModel):
    """Class represents monsters"""
    name = pw.TextField()
    coordinate = pw.TextField()

class NPC(BaseModel):
    """Class represents NPC"""
    name = pw.TextField()
    coordinate = pw.TextField()
    
