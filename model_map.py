'''Module consist map for Omen'''

import os

import peewee as pw

from header import *



'''
Declaration of common variable:
    coordinate: coordinate of objects
    database: variable of meta classes
'''

ID = pw.PrimaryKeyField(unique=True, primary_key=True)
COORDINATE = pw.TextField()
NAME = pw.TextField()
JMO = pw.TextField()
JO = pw.TextField()
JEV = pw.TextField()
PID = pw.TextField()

# Trying connect to file DB
try:
    map_db = pw.SqliteDatabase(MAP_DB)

# Detecting error and correct
except pw.OperationalError:
    os.makedirs(DB_PATH)
    # Creating DataBase file
    map_db_file = open(MAP_DB, 'w+')
    # Coor DataBase object
    map_db = pw.SqliteDatabase(MAP_DB)

class npcs(pw.Model):
    '''class represents npcs'''
    id = ID
    coordinate = COORDINATE

    class Meta:
        database = map_db

class players(pw.Model):
    '''class represents players'''
    id = ID
    coordinate = COORDINATE

    class Meta:
        database = map_db

class things(pw.Model):
    '''class represents things'''
    id = ID
    coordinate = COORDINATE

    class Meta:
        database = map_db

class map_obj(pw.Model):
    ''' class represent object on map '''
    id = ID
    coordinate = COORDINATE
    json_obj = JO

    class Meta:
        database = map_db

class etc(pw.Model):
    '''class represents etc'''
    id = ID
    coordinate = COORDINATE

    class Meta:
        database = map_db

# DEBUG RUN
'''
try:
    npcs.create_table()
    players.create_table()
    things.create_table()
    map_obj.create_table()
    etc.create_table()
except pw.OperationalError:
    pass
'''
# DEBUG STOP
