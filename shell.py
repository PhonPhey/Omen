<<<<<<< Updated upstream
""" Shell module for Omen Engine """
from jsonsempai import magic
from Omen.locale import ru_RU as locale
=======
''' Shell module for Omen Engine '''
from jsonsempai import magic
>>>>>>> Stashed changes

from Omen.locale import ru_RU as locale

import os

def _menu():
    menu_choice = int(input("[1]Play\n[2]Setting\n[3]About\n[4]Exit\n|=>"))
    
    if menu_choice == 1:
        os.system("clear")
    
    elif menu_choice == 2:
        "'"" Settings block """
        print("Settings not found!")
        exit(0)
    
    elif menu_choice == 3:
        """ Authors and other """
        print("Powder by Omen.\nCirina Studio 2017")
    
    elif menu_choice == 4:
        print(locale.goodbye)
        exit(0)
    
    else:
        print(locale.error)
        exit(1)
        
def init():
    print("Powder by Omen.\nCirina Studio 2017")
    _menu()
    print(locale.hello)
    while True:
        command = input("\n|=> ")
         
        if command in ("exit", "Exit"):
             print(locale.goodbye)
<<<<<<< Updated upstream
             y = False
             
=======
             exit(0)
        
        elif command in ("clear", "Clear"):
            os.system("clear")
            
>>>>>>> Stashed changes
        else:
            print(locale.notunderstand)
        
