import peewee as pw
import os

try:
    main_db = pw.SqliteDatabase('db/main.db')

except pw.OperationalError:
    os.makedirs('db/')
    main_db_file = open('db/main.db', 'w+')
    main_db = pw.SqliteDatabase('db/main.db')

class players(pw.Model):
    name = pw.CharField()
    hp = pw.IntegerField()
    mp = pw.IntegerField()
    json_meta_obj = pw.CharField()

    class Meta:
        database = main_db

class things(pw.Model):
    name = pw.CharField()
    level = pw.IntegerField()
    strgh = pw.IntegerField()
    json_meta_obj = pw.CharField()

    class Meta:
        database = main_db

# DEBUG RUN
#try:
#    players.create_table()
#    things.create_table()
#except pw.OperationalError:
#    pass
# DEBUG STOP
