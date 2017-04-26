'''Module consist dynamic for Omen'''

import os

import peewee as pw

import header as h

'''
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    dynamic_db = pw.SqliteDatabase(h.DYNAMIC_DB)

# Detecting error and correct
except pw.OperationalError:
    # Create db path if it none
    os.makedirs(h.DB_PATH)
    # Creating DataBase file
    dynamic_db_file = open(h.DYNAMIC_DB, 'w+')
    # Dynamic DataBase object
    dynamic_db = pw.SqliteDatabase(h.DYNAMIC_DB)


class players(pw.Model):
    '''class represents players'''
    id = h.ID
    name = h.NAME
    json_meta_obj = h.JMO

    class Meta:
        database = dynamic_db


class inventory(pw.Model):
    '''class represents inventory'''
    id = h.ID
    player_id = h.PID
    json_meta_obj = h.JMO

    class Meta:
        database = dynamic_db


class local_events(pw.Model):
    '''class represents local_events'''
    id = h.ID
    json_event_obj = h.JEV

    class Meta:
        database = dynamic_db


class global_events(pw.Model):
    '''class represents global_events'''
    id = h.ID
    json_event_obj = h.JEV

    class Meta:
        database = dynamic_db


# DEBUG RUN
try:
    players.create_table()
    inventory.create_table()
    local_events.create_table()
    global_events.create_table()
except pw.OperationalError:
    pass
# DEBUG STOP
