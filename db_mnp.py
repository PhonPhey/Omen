'''DataBase manipulation for Omen'''
# Functions for writing, changing and deleting

import random

import peewee as pw

from header import *
import model_dynamic as modeld
import model_map as modelm
import model_static as models

'''
Declaration of common variable:
    self.db: variable for database object, puts in self list
'''

ID = pw.PrimaryKeyField(unique=True, primary_key=True)
COORDINATE = pw.TextField()
NAME = pw.TextField()
JMO = pw.TextField()
JO = pw.TextField()
JEV = pw.TextField()
PID = pw.TextField()


class dbMnp():
    '''class for DataBase manipulation'''

    def __init__(self, db_name):
        ''' Init fuction for class '''

        self.db_nm = db_name

        # In this construction we create database object
        if db_name == "static":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        elif db_name == "dynamic":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        elif db_name == "map":
            self.db = pw.SqliteDatabase('db/' + db_name + '.db')

        elif db_name == 0:
            pass

        else:
            print("Error!!! Invalid database name: " + db_name)

    def _random_id(self, base_id):
        random.seed(id)

        return random.randint(1, 10000) + random.randint(random.randint(1, 5000), 8000)

    def add_record(self, nm_table, data):
        ''' Function for add record '''
        mnp_func = dbMnp(0)

        if nm_table in DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table == 'players':
                modeld.players.create(id=mnp_func._random_id(modeld.players.id),
                                      name=data[0], json_meta_obj=data[1])

                modeld.players.update()

            elif nm_table == 'invent':
                modeld.inventory.create(id=mnp_func._random_id(modeld.inventory.id),
                                        player_id=data[0], json_meta_obj=data[1])

                modeld.inventory.update()

            elif nm_table == 'le':
                modeld.local_events.create(id=mnp_func._random_id(modeld.local_events.id),
                                           json_event_obj=data)
                modeld.local_events.update()

            elif nm_table == 'ge':
                modeld.global_events.create(id=mnp_func._random_id(modeld.global_events.id),
                                            json_event_obj=data)
                modeld.global_events.update()

        if nm_table in STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table == 'things':
                models.things.create(id=mnp_func._random_id(models.things.id),
                                     name=data[0], json_meta_obj=data[1])
                models.things.update()

            elif nm_table == 'monsters':
                models.monsters.create(id=mnp_func._random_id(models.monsters.id),
                                       name=data[0], json_meta_obj=data[1])
                models.monsters.update()

            elif nm_table == 'npcs':
                models.npcs.create(id=mnp_func._random_id(models.npcs.id),
                                   name=data[0], json_meta_obj=data[1])
                models.npcs.update()

            elif nm_table == 'events':
                models.events.create(id=mnp_func._random_id(models.events.id),
                                     name=data[0], json_obj=data[1])
                models.events.update()

        if nm_table in MAP_DB_TABLES and self.db_nm == "map":
            if nm_table == 'npcs':
                modelm.npcs.create(id=mnp_func._random_id(modelm.npcs.id),
                                   coordinate=data[0])
                modelm.npcs.update()

            elif nm_table == 'players':
                modelm.players.create(id=mnp_func._random_id(modelm.players.id),
                                      link_id=mnp_func._random_id(modelm.players.id),
                                      coordinate=data)
                modelm.players.update()

            elif nm_table == 'things':
                modelm.things.create(id=mnp_func._random_id(modelm.things.id),
                                     coordinate=data)
                modelm.things.update()

            elif nm_table == 'mo':
                modelm.map_obj.create(id=mnp_func._random_id(modelm.map_obj.id),
                                      coordinate=data[0], json_obj=data[1])
                modelm.map_obj.update()

    def edit_record(self, nm_table, record_id, nm_column, data):
        '''function for updating record'''
        mnp_func = dbMnp(0)

        if nm_table in DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table == 'players':
                if nm_column == 'name':
                    modeld.players.update(name=data).where(
                        modeld.players.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    modeld.players.update(json_meta_obj=data).where(
                        modeld.players.id == record_id).execute()
            elif nm_table == 'invent':
                if nm_column == 'player_id':
                    modeld.inventory.update(player_id=data).where(
                        modeld.inventory.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    modeld.inventory.update(json_meta_obj=data).where(
                        modeld.inventory.id == record_id).execute()

            elif nm_table == 'le':
                if nm_column == 'json_event_obj':
                    modeld.local_events.update(json_event_obj=data).where(
                        modeld.local_events.id == record_id).execute()

            elif nm_table == 'ge':
                if nm_column == 'json_event_obj':
                    modeld.global_events.update(json_event_obj=data).where(
                        modeld.global_events.id == record_id).execute()

        if nm_table in STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table == 'things':
                if nm_column == 'name':
                    models.things.update(name=data).where(
                        models.things.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    models.things.update(json_meta_obj=data).where(
                        models.things.id == record_id).execute()

            elif nm_table == 'monsters':
                if nm_column == 'name':
                    models.monsters.update(name=data).where(
                        models.monsters.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    models.monsters.update(json_meta_obj=data).where(
                        models.monsters.id == record_id).execute()

            elif nm_table == 'npcs':
                if nm_column == 'name':
                    models.npcs.update(name=data).where(
                        models.npcs.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    models.npcs.update(json_meta_obj=data).where(
                        models.npcs.id == record_id).execute()

            elif nm_table == 'events':
                if nm_column == 'name':
                    models.events.update(name=data).where(
                        models.events.id == record_id).execute()
                elif nm_column == 'json_meta_obj':
                    models.events.update(json_meta_obj=data).where(
                        models.events.id == record_id).execute()

        if nm_table in MAP_DB_TABLES and self.db_nm == "map":
            if nm_table == 'npcs':
                if nm_column == 'coordinate':
                    modelm.npcs.update(coordinate=data).where(
                        modelm.npcs.id == record_id).execute()

            elif nm_table == 'players':
                if nm_column == 'coordinate':
                    modelm.players.update(coordinate=data).where(
                        modelm.players.id == record_id).execute()

            elif nm_table == 'things':
                if nm_column == 'coordinate':
                    modelm.things.update(coordinate=data).where(
                        modelm.things.id == record_id).execute()

            elif nm_table == 'mo':
                if nm_column == 'coordinate':
                    modelm.map_obj.update(coordinate=data).where(
                        modelm.map_obj.id == record_id).execute()
                elif nm_column == 'json_obj':
                    modelm.map_obj.update(json_obj=data).where(
                        modelm.map_obj.id == record_id).execute()

    def del_record(self, nm_table, record_id):
        ''' function for delete record '''
        mnp_func = dbMnp(0)

        if nm_table in DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table == 'players':
                modeld.players.delete().where(modeld.players.id == record_id).execute()

                modeld.players.update()

            elif nm_table == 'invent':
                modeld.inventory.delete().where(modeld.inventory.id == record_id).execute()

                modeld.inventory.update()

            elif nm_table == 'le':
                modeld.local_events.delete().where(modeld.local_events.id == record_id).execute()

                modeld.local_events.update()

            elif nm_table == 'ge':
                modeld.global_events.delete().where(
                    modeld.global_events.id == record_id).execute()

                modeld.global_events.update()

        if nm_table in STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table == 'things':
                models.things.delete().where(models.things.id == record_id).execute()

                models.things.update()

            elif nm_table == 'monsters':
                models.monsters.delete().where(models.monsters.id == record_id).execute()

                models.monsters.update()

            elif nm_table == 'npcs':
                models.npcs.delete().where(models.npcs.id == record_id).execute()

                models.npcs.update()

            elif nm_table == 'events':
                models.events.delete().where(models.events.id == record_id).execute()

                models.events.update()

        if nm_table in MAP_DB_TABLES and self.db_nm == "map":
            if nm_table == 'npcs':
                modelm.npcs.delete().where(modelm.npcs.id == record_id).execute()

                modelm.npcs.update()

            elif nm_table == 'players':
                modelm.players.delete().where(modelm.players.id == record_id).execute()

                modelm.players.update()

            elif nm_table == 'things':
                modelm.things.delete().where(modelm.things.id == record_id).execute()

                modelm.things.update()

            elif nm_table == 'mo':
                modelm.map_obj.delete().where(modelm.map_obj.id == record_id).execute()

                modelm.map_obj.update()


def _start_test_db():
    db_dynamic = dbMnp("dynamic")
    db_dynamic.add_record("le", ("test"))
    db_dynamic.add_record("ge", ("test"))
    db_dynamic.add_record("players", ("test", "test"))
    db_dynamic.add_record("invent", ("test", "test"))

    db_static = dbMnp("static")
    db_static.add_record("monsters", ("Bat", "test"))
    db_static.add_record("things", ("Bat", "test"))
    db_static.add_record("npcs", ("Bat", "test"))
    db_static.add_record("events", ("Bat", "test"))

    db_map = dbMnp("map")
    db_map.add_record("npcs", ("Bat", "test"))
    db_map.add_record("players", ("Bat", "test"))
    db_map.add_record("things", ("Bat", "test"))
    db_map.add_record("mo", ("Bat", "test"))


def _del_test_record(id):
    db_map = dbMnp("dynamic")
    db_map.del_record("players", id)


def _edit_test_record(id):
    db_map = dbMnp("dynamic")
    db_map.edit_record("players", id, "json_meta_obj", '0')


if __name__ == "__main__":
    _start_test_db()
    #_del_test_record(13272)
    _edit_test_record(8999)
