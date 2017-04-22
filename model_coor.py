'''Module consist coor for Omen'''

import peewee as pw
import os

'''
Declaration of common variable:
    coordinate: coordinate of objects
    database: variable of meta classes
'''

# Trying connect to file DB
try:
    coor_db = pw.SqliteDatabase('db/coor.db')

# Detecting error and correct
except pw.OperationalError:
    os.makedirs('db/')
    # Creating DataBase file
    coor_db_file = open('db/coor.db', 'w+')
    # Coor DataBase object
    coor_db = pw.SqliteDatabase('db/coor.db')

class npcs(pw.Model):
    '''class represents npcs'''
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class players(pw.Model):
    '''class represents players'''
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class things(pw.Model):
    '''class represents things'''
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class etc(pw.Model):
    '''class represents etc'''
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

# DEBUG RUN
#try:
   # npcs.create_table()
    #players.create_table()
    #things.create_table()
    #etc.create_table()
#except pw.OperationalError:
    #pass
# DEBUG STOP
