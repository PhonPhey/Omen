import peewee as pw

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
class monster(pw.Model):
    name = pw.CharField()
    json_meta_obj = pw.CharField()
    
    class Meta:
        database = main_db

class npcs(pw.Model):
    name = pw.CharField()
    json_meta_obj = pw.CharField()
    
    class Meta:
        database = main_db

class iventory(pw.Model):
    name = pw.CharField()
    json_meta_obj = pw.CharField()
    
    class Meta:
        database = main_db

class local_event(pw.Model):
    name = pw.CharField()
    json_event_obj = pw.CharField()
    
    class Meta:
        database = main_db

class global_events(pw.Model):
    json_event_obj = pw.CharField()
    
    class Meta:
        database = main_db

class coardinati(pw.Model):
    x = pw.Integerfield()
    y = pw.Integerfield()
    json_event_obj = pw.CharField()
    
    class Meta:
        database = main_db
# DEBUG RUN 
# players.create_table() 
# things.create_table() 
# monster.create_table()
# npcs.create_table()
# DEBUG STOP
