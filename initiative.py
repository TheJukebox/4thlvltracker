#!/usr/local/bin/python3
import random

class initiative:
    """handles operations on initiative orders"""
	
    def __init__(self):	
            
            # item details
            self.name = []
            self.init = []
            self.hp = []
            self.conc = []
            self.id = []
            self.order = {}

            # round and time counters
            self.round = 1
            self.time = 1
    
    def append_init(self,name_val,init_val,hp_val):
            """appends new items to the name, init, hp, conc, and id lists"""	
            
            name = self.name
            init = self.init
            hp = self.hp		
            conc = self.conc		
            id = self.id

            name.append(name_val)
            init.append(init_val)
            hp.append(hp_val)
            
            # set all concentration values to False
            conc.append(False)
            # generate a random id for items so we can
            # avoid conflicting names/initiatives
            id.append(self.gen_id())

    def gen_id(self):
            """generates unique IDs for items"""
            
            # generate an id from big range
            id = random.randint(1,10000)
            
            # if we clash, get a new one
            if id in self.id:
                    return gen_id()
            else:
                    return id

    def remove_init(self,id):
            """removes items from the name, init, and hp lists"""

            try:
                    # use the id index to avoid conflicting
                    # names etc.
                    index = self.id.index()
            except:
                    print("[!] That character does not exist in the initiative!")

            self.name.remove(self.name[index])
            self.init.remove(self.init[index])
            self.hp.remove(self.hp[index])
            self.conc.remove(self.conc[index])
            self.id.remove(self.id[index])

    def set_hp(self,id,num):
            """modifies the hp of an item"""
            
            check = input("[!] Really change HP? ")
            if str.lower(check) in ("y","yes","ye"):	
                    try:
                            # use the id index to avoid conflicting
                            # names etc.
                            index = self.id.index(id)
                    except:
                            print("[!] That character does not exist in the initiative!")
                    self.hp[index] += int(num)
                    if self.conc[index] == True:
                            print("[!] Concentration check!")
                            check = str.lower(input("Failed? "))
                            if check in ("y","ye","yes"):
                                    self.conc[index] = False
                                                            
            elif str.lower(check) in ("n","no"):
                    return
            else:
                    print("[!] [y]es or [n]o?")
                    self.set_hp(id,num)		

            
    def toggle_conc(self,id):
            """toggles whether an item is concentrating or not"""
            
            try:
                    # use the id index to avoid conflicting
                    # names etc.
                    index = self.id.index(id)
            except:
                    print("[!] That character does not exist in the initiative!")
            
            # check the current value of an item's concentration
            # so we can toggle it	
            if self.conc[index] == False:
                    self.conc[index] = True
            else:
                    self.conc[index] = False
            
                    
    def start_init(self):
            """handles iteration over the initiative order"""
            
            i = 0 # reset i to 0 to help iterate during the round
            print("\nROUND:",self.round)
            print("-------------------------")
            order = self.sort_init() # get the sorted initiative order
    
            for k, v in order.items():
                    print("{} || INITITIATIVE: {}\t| HP: {}".format(v,k,self.hp[i]))
                    print("Unique ID: #"+str(self.id[i]))

                    # are they concentrating?
                    if self.conc[i] == True:
                            print("CONCENTRATING!")

                    # wait for user input
                    option = input("# ")
                    
                    # check whatever they input
                    if str.lower(option) in ("exit","quit","q","e"):
                            check = input("[!] Really quit? ")
                            if str.lower(check) in ("y","yes","ye"):
                                    exit()
                            else:
                                    option = input("# ")
                    if str.lower(option) in ("con","conc","concentrate","concentration"):
                            self.toggle_conc(self.id[i])
                            print("TIME ELAPSED: {} seconds".format(self.time*6))
                            self.time += 1
                    
                    # if it's none of our string options...
                    else:
                            try:
                                    # is it an int we can use to change the hp of an item?
                                    num = int(option)
                                    self.set_hp(self.id[i],num)
                            except:
                                    print("TIME ELAPSED: {} seconds".format(self.time*6))
                                    self.time += 1
                    i += 1

            self.round += 1
            self.start_init()
    
    def sort_init(self):
            """sorts initiative orders by descending scores"""	
    
            # make sure we actually have something to sort.
            # if we don't, head back to main and start again.	
            if len(self.init) == 0:
                    print("[!] Empty initiative order!")
                    main()
    
            # really simple selection sort, gets the job done	
            for i in range(len(self.init)):
                    max = i
                    for j in range(i+1,len(self.init)):
                            if int(self.init[j]) > int(self.init[i]):
                                    max = j
                    # here's our swaps - considering making this a function
                    # of its own.
                    self.init[i], self.init[max] = self.init[max], self.init[i]
                    self.name[i], self.name[max] = self.name[max], self.name[i]
                    self.hp[i], self.hp[max] = self.hp[max], self.hp[i]
                    self.conc[i], self.conc[max] = self.conc[max], self.conc[i]
                    self.id[i], self.id[max] = self.id[max], self.id[i]
            
            # fill up a dictionary with sorted values.
            # way more convenient for when we iterate over the order.	
            for v in range(len(self.init)):
                    self.order[self.init[v]] = self.name[v]
            return self.order

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

