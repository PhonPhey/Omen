import peewee as pw
import os

try:
    dynamic_db = pw.SqliteDatabase('db/dynamic.db')

except pw.OperationalError:
    os.makedirs('db/')
    dynamic_db_file = open('db/dynamic.db', 'w+')
    dynamic_db = pw.SqliteDatabase('db/dynamic.db')

class players(pw.Model):
    name = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class inventory(pw.Model):
    player_id = pw.TextField()
    json_meta_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class local_events(pw.Model):
    json_event_obj = pw.TextField()

    class Meta:
        database = dynamic_db

class global_events(pw.Model):
    json_event_obj = pw.TextField()

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
