'''Module consist static for Omen'''

import os

import peewee as pw

import header as h

'''
Declaration of common variable:
    name: name of object of [class_object]
    json_meta_obj: json object of meta class
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    # Static DataBase object
    static_db = pw.SqliteDatabase(h.STATIC_DB)

# Detecting error and correct
except pw.OperationalError:
    os.makedirs(h.DB_PATH)
    # Creating DataBase file
    static_db_file = open(h.STATIC_DB, 'w+')
    # Static DataBase object
    static_db = pw.SqliteDatabase(h.STATIC_DB)

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
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

class monsters(pw.Model):
    '''class represents monsters'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

class npcs(pw.Model):
    '''class represents npcs'''
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

class events(pw.Model):
    '''class represents events'''
    name = pw.TextField()
    json_obj = pw.TextField()

    class Meta:
        database = static_db

# DEBUG RUN
try:
    things.create_table()
    monsters.create_table()
    npcs.create_table()
    events.create_table()
except pw.OperationalError:
    pass
# DEBUG STOP
