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


class players(pw.Model):
    '''class represents players'''
    id = ID
    name = NAME
    json_meta_obj = JMO

    class Meta:
        database = dynamic_db


class inventory(pw.Model):
    '''class represents inventory'''
    id = ID
    player_id = PID
    json_meta_obj = JMO

    class Meta:
        database = dynamic_db


class local_events(pw.Model):
    '''class represents local_events'''
    id = ID
    json_event_obj = JEV

    class Meta:
        database = dynamic_db


class global_events(pw.Model):
    '''class represents global_events'''
    id = ID
    json_event_obj = JEV

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
