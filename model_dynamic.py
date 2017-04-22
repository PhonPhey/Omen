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

class players(pw.Model):
    '''class represents players'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class inventory(pw.Model):
    '''class represents inventory'''
    player_id = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class local_events(pw.Model):
    '''# class represents local_events'''
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class global_events(pw.Model):
    '''class represents global_events'''
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
