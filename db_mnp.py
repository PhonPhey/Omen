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

        elif db_name == None:
            pass

        else:
            print("Error!!! Invalid database name: " + db_name)

    def _random_id(self, base_id):
        random.seed(id)

        return random.randint(1, 10000)

    def add_record(self, nm_table, data):
        mnp_func = dbMnp(None)

        if nm_table in h.DYNAMIC_DB_TABLES and self.db_nm == "dynamic":
            if nm_table is 'players':
                modeld.players.create(id=mnp_func._random_id(modeld.players.id),
                                      name=data[0], json_meta_obj=data[1])
            elif nm_table is 'invent':
                modeld.inventory.create(id=mnp_func._random_id(modeld.inventory.id),
                                        player_id=data[0], json_meta_obj=data[1])
            elif nm_table is 'le':
                modeld.locald_events.create(id=mnp_func._random_id(modeld.local_events.id),
                                            json_meta_obj=data[0])
            elif nm_table is 'ge':
                modeld.global_events.create(id=mnp_func._random_id(modeld.global_events.id),
                                            json_meta_obj=data[0])

        if nm_table in h.STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table is 'things':
                models.things.create(id=mnp_func._random_id(models.things.id),
                                     name=data[0], json_meta_obj=data[1])
            elif nm_table is 'monsters':
                models.monsters.create(id=mnp_func._random_id(models.monsters.id),
                                       name=data[0], json_meta_obj=data[1])
                                       
            elif nm_table is 'npcs':
                models.npcs.create(id=mnp_func._random_id(models.npcs.id),
                                   json_meta_obj=data[0])
            elif nm_table is 'events':
                models.events.create(id=mnp_func._random_id(models.events.id),
                                     json_meta_obj=data[0])

        if nm_table in h.MAP_DB_TABLES and self.db_nm == "map":
            if nm_table is 'npcs':
                modelm.things.create(id=mnp_func._random_id(modelm.npcs.id),
                                     name=data[0], json_meta_obj=data[1])
            elif nm_table is 'players':
                modelm.monsters.create(id=mnp_func._random_id(modelm.players.id),
                                       player_id=data[0], json_meta_obj=data[1])
            elif nm_table is 'things':
                modelm.npcs.create(id=mnp_func._random_id(modelm.things.id),
                                   json_meta_obj=data[0])
                modelm.npcs.save()

            elif nm_table is 'mo':
                modelm.events.create(id=mnp_func._random_id(modelm.map_obj.id),
                                     json_meta_obj=data[0])




# DEBUG RUN
if __name__ == "__main__":
    db_static = dbMnp("static")
    db_dynamic = dbMnp("dynamic")
    db_static.add_record("monsters", ("Bat", "{'str': 5}"))
    db_static.save()

# DEBUG STOP
