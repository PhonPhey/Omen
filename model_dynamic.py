'''Module consist dynamic for Omen'''

import peewee as pw
import os

'''
Declaration of common variable:
    json_meta_obj: json object of meta class
    json_event_obj: json object of event classes
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    dynamic_db = pw.SqliteDatabase('db/dynamic.db')

# Detecting error and correct
except pw.OperationalError:
    os.makedirs('db/')
    # Creating DataBase file
    dynamic_db_file = open('db/dynamic.db', 'w+')
    # Dynamic DataBase object
    dynamic_db = pw.SqliteDatabase('db/dynamic.db')

# class represents players
class players(pw.Model):
    '''it class create table with players'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

# class represents inventory
class inventory(pw.Model):
    '''it class create table with enventory'''
    player_id = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

# class represents local_events
class local_events(pw.Model):
    '''it class create table with local_events'''
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db

# class represents global_events
class global_events(pw.Model):
    '''it class create table with global_events'''
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db

# DEBUG RUN
#try:
  #  players.create_table()
  #  inventory.create_table()
  #  local_events.create_table()
  #  global_events.create_table()
#except pw.OperationalError:
   # pass
# DEBUG STOP
