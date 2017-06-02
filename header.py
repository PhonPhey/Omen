''' Header module for Omen Engine '''

import peewee as pw


# PATHs
DB_PATH = 'db/'
MAP_DB = 'db/map.db'
STATIC_DB = 'db/static.db'
DYNAMIC_DB = 'db/dynamic.db'

# DBs info

#> DINAMIC_DB
DYNAMIC_DB_TABLES = ['players', 'invent', 'le', 'ge']
DYNAMIC_DB_PLAYERS = [3, "id", "name", "json_meta_obj"]
DYNAMIC_DB_INVENT = [3, "id", "player_id", "json_meta_obj"]
DYNAMIC_DB_LE = [2, "id", "json_event_obj"]
DYNAMIC_DB_GE = [2, "id", "json_event_obj", ]

#>STATIC_DB
STATIC_DB_TABLES = ['things', 'monsters', 'npcs', 'events']
STATIC_DB_THINGS = [3, "id", "name", "json_meta_obj"]
STATIC_DB_MONSTERS = [3, "id", "name", "json_meta_obj"]
STATIC_DB_NPCS = [3, "id", "name", "json_meta_obj"]
STATIC_DB_EVENTS = [3, "id", "name", "json_meta_obj"]

#>MAP_DB
MAP_DB_TABLES = ['npcs', 'players', 'things', 'mo']
MAP_DB_NPCS = [2, "id", "coordinate"]
MAP_DB_PLAYERS = [2, "id", "coordinate"]
MAP_DB_THINGS = [2, "id", "coordinate"]
MAP_DB_MO = [3, "id", "coordinate", "json_obj"]

