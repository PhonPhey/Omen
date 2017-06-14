'''Player module for Omen Engine'''

from jsonsempai import magic
from Omen.locale import ru_RU as locale

from Omen.util import *

class Player:
    def __init__(self):
        pass
        
    def create_player(self, point, min_point):
        input_ability = locale.input + " " + locale.ability_gen.ability_1 + " " 
        
        player_name = input(locale.input + " " + locale.name +": ")
        player_coordinate = [0,0]
        json_meta_obj = {"str": 0, "int": 0, "con": 0, "wis": 0, "char": 0, "dex": 0}
    
    
        json_meta_obj["str"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.str) + ": ")), point, min_point)
        point -= json_meta_obj["str"]
    
        json_meta_obj["int"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.int) + ": ")), point, min_point)
        point -= json_meta_obj["int"]
    
        json_meta_obj["con"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.con) + ": ")), point, min_point)
        point -= json_meta_obj["con"]
    
        json_meta_obj["wis"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.wis) + ": ")), point, min_point)
        point -= json_meta_obj["wis"]
    
        json_meta_obj["char"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.chr) + ": ")), point, min_point)
        point -= json_meta_obj["char"]
    
        json_meta_obj["dex"] = valid_point(int(input(input_ability + 
                                in_quot(locale.abilitys.dex) + ": ")), point, min_point)
        point -= json_meta_obj["dex"]

    
    
        print(json_meta_obj)