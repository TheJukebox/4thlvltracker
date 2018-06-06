#!/usr/local/bin/python3
import random
from initiative import *

help = """\n\t~~~ / | 4th Level Tracker | \ ~~~
(type "help" to print this usage information again)\n
enter the name and initiative of each character/creature
in combat. typing "done" will sort your initiative order
and start to iterate! if you type roll in place of
an initiative score, you can randomly generate an
initiative score using the character's modifier.\n
during iteration typing "conc" will toggle concentration
for the specific character/creature. if you type an integer
(positive or negative) it will add that integer to the
creatures hp score.\n
type "quit" or "exit" to exit the program.\n"""

def roll():
    """rolls psuedo-random d20s for initiative"""

    try:
            mod = int(input("MODIFIER: "))
    except:
            print("[!] Modifiers must be integers!")
            return roll()

    return random.randint(1,20)+mod # return a random d20 roll, plus the user's mod
                    

def get_hp():
    """gets the hp of an item from user input"""

    hp = input("HEALTH: ")
    try:
            return int(hp)
    except:
            if hp in ("quit","q","exit","e"):
                    if not quit():
                            return get_hp()
            elif str.lower(hp) == "help":
                    print(help)
                    get_hp()
            elif str.lower(hp) == "done":
                    return str.lower(hp)
            else:
                    print("[!] HP scores must be integers!")
                    return get_hp()
    
def get_init():
    """gets an initiative score from user input"""
    
    init = input("INITIATIVE: ")
    try:
            return int(init)
    except:
            init = str.lower(init)
            if init in ("quit","q","exit","e"):
                    if not quit():
                            return get_init()
            elif init == "help":
                    print(help)
                    return get_init()
            elif init == "done":
                    return init
            elif init == "roll":
                    init = roll()
                    print("Rolled {} for initiative.".format(init))
                    return init	
            else:
                    print("[!] Initiative scores must be integers!")
                    return get_init()
    
def create_items():
    """creates new items based on user input"""
            
    name = input("NAME: ")
    if str.lower(name) in ("quit","q","exit","e"):
            if not quit():
                    return create_items()
    elif str.lower(name) == "done":
            return name, 0, 0 # escape!	
    init = get_init()
    if init == "done":
            return name, init, 0 # escape!
    hp = get_hp()
    if hp == "done":
            return name, init, hp # escape!

    return name, init, hp

def quit():
    check = str.lower(input("[!] Really quit? "))
    if check in ("y","yes","ye"):
            print("[!] Exiting 4th Level Tracker...\nBuilt by The Jukebox for D&D 5e.")
            exit()
    else:
            return False
def main():
            
    init_handler = initiative()
    print(help)
    print("[INITIATIVE CREATION]\n---------------------")	

    while True:
            name, init, hp = create_items()
            # if they've input "done" at any point, we can catch it and
            # start the initiative tracker.
            if name == str.lower("done") or init == str.lower("done") or hp == str.lower("done"):
                    print("\n[INITIATIVE ORDER]\n------------------")
                    init_handler.start_init()
                    return False
            else:
                    # uses our initiative object to add
                    # new items to the order.
                    init_handler.append_init(name, init, hp)
                            
main()
            
