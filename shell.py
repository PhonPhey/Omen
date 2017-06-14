""" Shell module for Omen Engine """
from jsonsempai import magic
from Omen.locale import ru_RU as locale

def init():
    y = True
    print("Powder by Omen.\nCirina Studio 2017")
    while y:
        command = input("\n|=> ")
         
        if command in ("exit", "Exit"):
             print(locale.goodbye)
             y = False
             
        else:
            print(locale.notunderstand)
        
