##################### MODULES

import jdr
import random

#####################



##################### VARIABLES

SCENARIO_USE = 0

#####################



##################### CLASSES

# jdr classes in jdr.py (name, description, capacity, actions) -> poticha.jdr.x
    

#####################



##################### FUNCTIONS

def scenario(scenario):
    global SCENARIO_USE
    if SCENARIO_USE == 0:
        print(scenario)
        SCENARIO_USE += 1
    else:
        print("Error | Scenario was already used once.")

def story(story_events):
    print(story_events)

def dice(minimum:int, maximum: int):
    dice = random.randint(minimum, maximum)
    return dice

listpanel = []

def panel(listpanel):
    for x in listpanel:
        print("Name:",x.name,"| Description:",x.description,"| Class:",x.clas,"| Capacity:",x.capacity,"| Actions:",x.actions)




#####################



    
        

# You may say that we don't need this module to make RPG game. We could just say "
# class X:
#   name = "name" in your code right, poticha is still in development it'll be a bit useless for now, but useful in future,
# as long as I update it.