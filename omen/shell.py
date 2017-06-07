''' Shell module for Omen Engine '''
from jsonsempai import *

def _valid():
    pass

def create_player():
    player_name = input("Введите имя: ")
    player_coordinate = [0,0]
    point = 100
    json_meta_obj = {"str": 0, "int": 0, "con": 0, "wis": 0, "char": 0, "dex": 0}
    json_meta_obj["str"] = int(input("Введите силу: "))
    json_meta_obj["int"] = int(input("Введите ловкость: "))
    json_meta_obj["con"] = int(input("Введите телосложение: "))
    json_meta_obj["wis"] = int(input("Введите интеллект: "))
    json_meta_obj["char"] = int(input("Введите мудрость: "))
    json_meta_obj["dex"] = int(input("Введите харизму: "))
    
    print(json_meta_obj)