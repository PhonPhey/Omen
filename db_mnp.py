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

                modeld.players.save()

            elif nm_table is 'invent':
                modeld.inventory.create(id=mnp_func._random_id(modeld.inventory.id),
                                        player_id=data[0], json_meta_obj=data[1])

                modeld.invent.save()

            elif nm_table is 'le':
                modeld.local_events.create(id=mnp_func._random_id(modeld.local_events.id),
                                           json_event_obj=data[0])
                modeld.local_events.save()

            elif nm_table is 'ge':
                modeld.global_events.create(id=mnp_func._random_id(modeld.global_events.id),
                                            json_event_obj=data[0])
                modeld.global_events.save()

        if nm_table in h.STATIC_DB_TABLES and self.db_nm == "static":
            if nm_table is 'things':
                models.things.create(id=mnp_func._random_id(models.things.id),
                                     name=data[0], json_meta_obj=data[1])
                models.things.save()

            elif nm_table is 'monsters':
                models.monsters.create(id=mnp_func._random_id(models.monsters.id),
                                       name=data[0], json_meta_obj=data[1])
                models.monsters.save()

            elif nm_table is 'npcs':
                models.npcs.create(id=mnp_func._random_id(models.npcs.id),
                                   json_meta_obj=data[0])
                models.npcs.save()

            elif nm_table is 'events':
                models.events.create(id=mnp_func._random_id(models.events.id),
                                     json_meta_obj=data[0])
                models.events.save()

        if nm_table in h.MAP_DB_TABLES and self.db_nm == "map":
            if nm_table is 'npcs':
                modelm.npcs.create(id=mnp_func._random_id(modelm.npcs.id),
                                   name=data[0], json_meta_obj=data[1])
                modelm.npcs.save()

            elif nm_table is 'players':
                modelm.players.create(id=mnp_func._random_id(modelm.players.id),
                                      player_id=data[0], json_meta_obj=data[1])
                modelm.players.save()

            elif nm_table is 'things':
                modelm.things.create(id=mnp_func._random_id(modelm.things.id),
                                     json_meta_obj=data[0])
                modelm.things.save()

            elif nm_table is 'mo':
                modelm.map_obj.create(id=mnp_func._random_id(modelm.map_obj.id),
                                      json_meta_obj=data[0])
                modelm.map_obj.save()


# DEBUG RUN
if __name__ == "__main__":
    db_dynamic = dbMnp("dynamic")
    db_dynamic.add_record("le", ("{'test': 5}"))
    db_dynamic.add_record("players", ("{'test': 5}"))
    db_dynamic.add_record("invent", ("{'test': 5}"))

    db_static = dbMnp("static")
    db_static.add_record("monsters", ("Bat", "{'str': 5}"))
    db_static.add_record("things", ("Bat", "{'str': 5}"))
    db_static.add_record("npcs", ("Bat", "{'str': 5}"))
    db_static.add_record("events", ("Bat", "{'str': 5}"))

    db_map = dbMnp("map")
    db_map.add_record("npcs", ("Bat", "{'str': 5}"))
    db_map.add_record("players", ("Bat", "{'str': 5}"))
    db_map.add_record("things", ("Bat", "{'str': 5}"))
    db_map.add_record("mo", ("Bat", "{'str': 5}"))
# DEBUG STOP
