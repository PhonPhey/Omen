'''Module consist map for Omen'''

import os

import peewee as pw

import header as h



'''
Declaration of common variable:
    coordinate: coordinate of objects
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    map_db = pw.SqliteDatabase(h.MAP_DB)

# Detecting error and correct
except pw.OperationalError:
    os.makedirs(h.DB_PATH)
    # Creating DataBase file
    map_db_file = open(h.MAP_DB, 'w+')
    # Coor DataBase object
    map_db = pw.SqliteDatabase(h.MAP_DB)

class npcs(pw.Model):
    '''class represents npcs'''
    coordinate = pw.TextField()

    class Meta:
        database = map_db

class players(pw.Model):
    '''class represents players'''
    coordinate = pw.TextField()

    class Meta:
        database = map_db

class things(pw.Model):
    '''class represents things'''
    coordinate = pw.TextField()

    class Meta:
        database = map_db

class map_obj(pw.Model):
    ''' class represent object on map '''
    coordinate = pw.TextField()
    json_obj = pw.TextField()

    class Meta:
        database = map_db

class etc(pw.Model):
    '''class represents etc'''
    coordinate = pw.TextField()

    class Meta:
        database = map_db

# DEBUG RUN
try:
    npcs.create_table()
    players.create_table()
    things.create_table()
    map_obj.create_table()
    etc.create_table()
except pw.OperationalError:
    pass
# DEBUG STOP
