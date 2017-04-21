import peewee as pw
import os

try:
    coor_db = pw.SqliteDatabase('db/coor.db')

except pw.OperationalError:
    os.makedirs('db/')
    coor_db_file = open('db/coor.db', 'w+')
    coor_db = pw.SqliteDatabase('db/coor.db')

class npcs(pw.Model):
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class players(pw.Model):
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class things(pw.Model):
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

class etc(pw.Model):
    coordinate = pw.TextField()

    class Meta:
        database = coor_db

# DEBUG RUN
try:
    npcs.create_table()
    players.create_table()
    things.create_table()
    etc.create_table()
except pw.OperationalError:
    pass
# DEBUG STOP
