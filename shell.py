''' Shell module for Omen Engine '''

def init():
    y = True
    print("Powder by Omen.\nCirina Studio 2017")
    while y:
        command = input("\n|=> ")
         
        if command in ("exit", "Exit"):
             print("Good buy!")
             y = False
             
        else:
            print("Я тебя не понимаю.")
        
