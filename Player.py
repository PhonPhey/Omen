'''Player module for Omen Engine'''

from jsonsempai import *
from util import valid_point

class Player:
    def __init__(self):
        pass
 
    def create_player(self, point, min_point):
        player_name = input("Введите имя: ")
        player_coordinate = [0,0]
        json_meta_obj = {"str": 0, "int": 0, "con": 0, "wis": 0, "char": 0, "dex": 0}
    
    
        json_meta_obj["str"] = valid_point(int(input("Введите силу: ")), point, min_point)
        point -= json_meta_obj["str"]
    
        json_meta_obj["int"] = valid_point(int(input("Введите ловкость: ")), point, min_point)
        point -= json_meta_obj["int"]
    
        json_meta_obj["con"] = valid_point(int(input("Введите телосложение: ")), point, min_point)
        point -= json_meta_obj["con"]
    
        json_meta_obj["wis"] = valid_point(int(input("Введите интеллект: ")), point, min_point)
        point -= json_meta_obj["wis"]
    
        json_meta_obj["char"] = valid_point(int(input("Введите мудрость: ")), point, min_point)
        point -= json_meta_obj["char"]
    
        json_meta_obj["dex"] = valid_point(int(input("Введите харизму: ")), point, min_point)
        point -= json_meta_obj["dex"]

    
    
    print(json_meta_obj)