import poticha as po
import time

### Let's make a little rpg game.

## Let's imagine that we have 2 Friends: Jake & Finn
## And we ask them  names for their characters
## Of course you decide their capacities & the class availables as you are the game master.

# Here let's say that there is 4 Classes: Troll, Magician, Swordsman, Bow


class monster:
    name = po.jdr.name("Buk")
    capacity = po.jdr.capacity(16)


class Finn:
    name = po.jdr.name("Djork")
    clas = po.jdr.clas("Swordsman")
    description = po.jdr.description("He has swords.")
    capacity = po.jdr.capacity("Can make lot of damages with a sword near his opponents.")
    actions = po.jdr.actions(2) # actions per turn.

class Jake:
    name = po.jdr.name("Mark")
    clas = po.jdr.clas("Troll")
    description = po.jdr.description("He's a troll, you shouldn't trust him.")
    capacity = po.jdr.capacity("If he rolls a 12, he runs away while a fight & will never come back.")
    actions = po.jdr.actions(1) # actions per turn.


po.listpanel = [Finn, Jake]

po.scenario("In a castle there was a treasure, sadly it got stolen from villains. Go to the undergrounds to get it back. Be aware of monsters!")

po.story(f"*{Finn.name} & {Jake.name} enter the undergrounds.*")
po.story("You meet a monster.")


fight_1_turn = 1
launch = 0    


def fight_1():
 
    global fight_1_turn
    po.panel(po.listpanel)
    c = True
    Finn.actions = 2
    Jake.actions = 1

    while fight_1_turn < 3:
        while Finn.actions > 0:

            while c:
                finnn = str(input("Let's roll a dice before."))
                dic = po.dice(1, 16)
                c = False

            if dic < 3:
                print(f"You got {dic} too bad!")
                Finn.actions -= 2
                
            else:
                finnnn = str(input("What you wanna do? > "))
                if finnnn == "atk":
                    monster.capacity -= Finn.actions
                    Finn.actions -= 1
                    if monster.capacity <= 0:
                        po.story("Dead!")
                        fight_1_turn = False
                    if Finn.actions == 0:
                        po.story(f"He didn't die, {Jake.name}'s turn.")
                        #d = True
                        c = False
        d = True
        while Jake.actions > 0:
            while d:
                jakeee = str(input("Let's roll a dice before"))
                dic = po.dice(1, 16)
                d = False
            
            if dic < 3:
                print(f"You got {dic} too bad!")
                fight_1()
                Jake.actions -= 1
            

            else:
                jak = str(input("What you wanna do? > "))
                if jak == "atk":
                    monster.capacity -= Jake.actions
                    Jake.actions -= 1
                if monster.capacity <= 0:
                    po.story("Dead!")
                    fight_1_turn = False
                if Jake.actions == 0:
                    po.story(f"He didn't die, {Finn.name}'s turn.")
                    fight_1_turn += 1
                    if fight_1_turn < 3:
                        fight_1()


    print("End of the fight, you didn't kill it. You die.")



def main():
    global launch
    if launch == 0:
        fight_1()
    launch += 1

if __name__ == '__main__':
    main()
