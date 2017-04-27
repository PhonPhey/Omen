'''DataBase manipulation for Omen'''
# Functions for writing, changing and deleting

import peewee as pw

import header as h

import random

import model_static as models

import model_dynamic as modeld

import model_map as modelm
'''
Declaration of common variable:
    self.db: variable for database object, puts in self list
'''


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

        if nm_table in h.DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table is 'players':
                modeld.players.create(id=mnp_func._random_id(modeld.players.id),
                                      name=data[0], json_meta_obj=data[1])

                modeld.players.update()

            elif nm_table is 'invent':
                modeld.inventory.create(id=mnp_func._random_id(modeld.inventory.id),
                                        player_id=data[0], json_meta_obj=data[1])

                modeld.inventory.update()

            elif nm_table is 'le':
                modeld.local_events.create(id=mnp_func._random_id(modeld.local_events.id),
                                           json_event_obj=data)
                modeld.local_events.update()

            elif nm_table is 'ge':
                modeld.global_events.create(id=mnp_func._random_id(modeld.global_events.id),
                                            json_event_obj=data)
                modeld.global_events.update()

        if nm_table in h.STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table is 'things':
                models.things.create(id=mnp_func._random_id(models.things.id),
                                     name=data[0], json_meta_obj=data[1])
                models.things.update()

            elif nm_table is 'monsters':
                models.monsters.create(id=mnp_func._random_id(models.monsters.id),
                                       name=data[0], json_meta_obj=data[1])
                models.monsters.update()

            elif nm_table is 'npcs':
                models.npcs.create(id=mnp_func._random_id(models.npcs.id),
                                   name=data[0], json_meta_obj=data[1])
                models.npcs.update()

            elif nm_table is 'events':
                models.events.create(id=mnp_func._random_id(models.events.id),
                                     name=data[0], json_obj=data[1])
                models.events.update()

        if nm_table in h.MAP_DB_TABLES and self.db_nm == "map":
            if nm_table is 'npcs':
                modelm.npcs.create(id=mnp_func._random_id(modelm.npcs.id),
                                   coordinate=data[0])
                modelm.npcs.update()

            elif nm_table is 'players':
                modelm.players.create(id=mnp_func._random_id(modelm.players.id), link_id=mnp_func._random_id(modelm.players.id),
                                      coordinate=data)
                modelm.players.update()

            elif nm_table is 'things':
                modelm.things.create(id=mnp_func._random_id(modelm.things.id),
                                     coordinate=data)
                modelm.things.update()

            elif nm_table is 'mo':
                modelm.map_obj.create(id=mnp_func._random_id(modelm.map_obj.id),
                                      coordinate=data[0], json_obj=data[1])
                modelm.map_obj.update()

    def del_record(self, nm_table, record_id):
        ''' function for delete record '''
        mnp_func = dbMnp(0)

        if nm_table in h.DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table is 'players':
                record = modeld.players.get(modeld.players.id == record_id)
                record.delete_instance()

                modeld.players.update()

            elif nm_table is 'invent':
                record = modeld.inventory.get(
                    modeld.inventory.id == record_id)
                record.delete_instance()

                modeld.inventory.update()

            elif nm_table is 'le':
                record = modeld.local_events.get(
                    modeld.local_events.id == record_id)
                record.delete_instance()

                modeld.local_events.update()

            elif nm_table is 'ge':
                record = modeld.global_events.get(
                    modeld.global_events.id == record_id)
                record.delete_instance()

                modeld.global_events.update()

        if nm_table in h.STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table is 'things':
                record = models.things.get(models.things.id == record_id)
                record.delete_instance()

                models.things.update()

            elif nm_table is 'monsters':
                record = models.monsters.get(
                    models.monsters.id == record_id)
                record.delete_instance()
                models.monsters.update()

            elif nm_table is 'npcs':
                record = models.npcs.get(models.npcs.id == record_id)
                record.delete_instance()

                models.npcs.update()

            elif nm_table is 'events':
                record = models.events.get(models.events.id == record_id)
                record.delete_instance()

                models.events.update()

        if nm_table in h.MAP_DB_TABLES and self.db_nm == "map":
            if nm_table is 'npcs':
                record = modelm.npcs.get(modelm.npcs.id == record_id)
                record.delete_instance()

                modelm.npcs.update()

            elif nm_table is 'players':
                modelm.players.delete().where(modelm.players.id == record_id).execute()

                modelm.players.update()

            elif nm_table is 'things':
                record = modelm.things.get(modelm.things.id == record_id)
                record.delete_instance()

                modelm.things.update()

            elif nm_table is 'mo':
                record = modelm.map_obj.get(modelm.map_obj.id == record_id)
                record.delete_instance()

                modelm.map_obj.update()


if __name__ == "__main__":
    '''
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
    '''
    #db_map.del_record("players", 2446)

# DEBUG STOP/
