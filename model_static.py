import os

import peewee as pw

try:
    static_db = pw.SqliteDatabase('db/static.db')

except pw.OperationalError:
    os.makedirs('db/')
    static_db_file = open('db/static.db', 'w+')
    static_db = pw.SqliteDatabase('db/static.db')

class things(pw.Model):
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = static_db

class monsters(pw.Model):
    name = pw.TextField()
    json_meta_obj = pw.TextField()       

    class Meta:
        database = static_db

class npcs(pw.Model):
    name = pw.TextField()
    json_meta_obj = pw.TextField()       

    class Meta:
        database = static_db

class events(pw.Model):
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
