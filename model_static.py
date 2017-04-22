'''Module consist static for Omen'''

import os
import peewee as pw

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

# class represents things
class things(pw.Model):
    '''class represents things'''

    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

# class represents monsters
class monsters(pw.Model):
    '''class represents monsters'''

    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

# class represents npcs
class npcs(pw.Model):
    '''class represents npcs'''

    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

# class represents events
class events(pw.Model):
    '''class represents events'''

    name = pw.TextField()
    json_obj = pw.TextField()

    class Meta:
        database = static_db

# DEBUG RUN
#try:
 #  things.create_table()
  # monsters.create_table()
   #npcs.create_table()
   #events.create_table()
#except pw.OperationalError:
#   pass
# DEBUG STOP
