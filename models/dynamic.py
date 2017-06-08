'''Module consist dynamic for Omen'''

import os

import peewee as pw

from header import *

ID = pw.PrimaryKeyField(unique=True, primary_key=True)
COORDINATE = pw.TextField()
NAME = pw.TextField()
JMO = pw.TextField()
JO = pw.TextField()
JEV = pw.TextField()
PID = pw.TextField()

'''
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    dynamic_db = pw.SqliteDatabase(DYNAMIC_DB)

# Detecting error and correct
except pw.OperationalError:
    # Create db path if it none
    os.makedirs(DB_PATH)
    # Creating DataBase file
    dynamic_db_file = open(DYNAMIC_DB, 'w+')
    # Dynamic DataBase object
    dynamic_db = pw.SqliteDatabase(DYNAMIC_DB)

class baseModel(pw.Model):
    ''' Base class for all models'''
    json_meta_obj = pw.TextField()
    id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database = dynamic_db

class players(pw.Model):
    '''class represents players'''
    name = pw.TextField()

    class Meta:
        database = dynamic_db


class inventory(pw.Model):
    '''class represents inventory'''
    player_id = pw.PrimaryKeyField(unique=True, primary_key=True)

    class Meta:
        database = dynamic_db


class local_events(pw.Model):
    '''class represents local_events'''
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db


class global_events(pw.Model):
    '''class represents global_events'''
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db


# DEBUG RUN
'''
try:
    players.create_table()
    inventory.create_table()
    local_events.create_table()
    global_events.create_table()
except pw.OperationalError:
    pass
'''
# DEBUG STOP
