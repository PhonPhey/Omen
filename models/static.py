'''Module consist static for Omen'''

import os

import peewee as pw

from header import *

'''
Declaration of common variable:
    name: name of object of [class_object]
    json_meta_obj: json object of meta class
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
    # Static DataBase object
    static_db = pw.SqliteDatabase(STATIC_DB)

# Detecting error and correct
except pw.OperationalError:
    os.makedirs(DB_PATH)
    # Creating DataBase file
    static_db_file = open(STATIC_DB, 'w+')
    # Static DataBase object
    static_db = pw.SqliteDatabase(STATIC_DB)

'''
Declaration of common variable:
    name: name of object of [class_object]
    json_meta_obj: json object of meta class
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    # Static DataBase object
    static_db = pw.SqliteDatabase('db/static.db')

# Detecting error and correct
except pw.OperationalError:
    os.makedirs('db/')
    # Creating DataBase file
    static_db_file = open('db/static.db', 'w+')
    # Static DataBase object
    static_db = pw.SqliteDatabase('db/static.db')

class things(pw.Model):
    '''class represents things'''
    id = ID
    name = NAME
    json_meta_obj = JMO

    class Meta:
        database = static_db

class monsters(pw.Model):
    '''class represents monsters'''
    id = ID
    name = NAME
    json_meta_obj = JMO

    class Meta:
        database = static_db

class npcs(pw.Model):
    '''class represents npcs'''
    id = ID
    name = NAME
    json_meta_obj = JMO

    class Meta:
        database = static_db

class events(pw.Model):
    '''class represents events'''
    id = ID
    name = NAME
    json_obj = JO

    class Meta:
        database = static_db

# DEBUG RUN
'''
try:
    things.create_table()
    monsters.create_table()
    npcs.create_table()
    events.create_table()
except pw.OperationalError:
    pass
'''
# DEBUG STOP
