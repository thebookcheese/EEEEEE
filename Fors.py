import random

def Drop1(p):
    pass

def ForesMain(p):
    print("You in Fors")
    SlimeFight(p)


def SlimeFight(p):
    SHP = random.randint(20,25)
    SAtt = random.randint(2,3)
    SDef = random.randint(0,1)
    SDodge = random.randint(2,5)
    
    print("You encounter a slime with ",SHP," health")
    while SHP > 0:
        if p.health > 0:
            Do = input("What do you want to do? \n Attack (1)")
            if Do == "1":
                SDamage = SAtt - p.health
                Dodge = random.randint(1,100)
                if Dodge < (p.dodge + 1):
                    print("Player dodged")
                else:
                    p.health = p.health - SDamage
                    print("You took ",SDamage," damage")
                pdamage = p.attack - SDef
                if Dodge < (SDodge + 1):
                    print("Slime dodged")
                else:
                    SHP = SHP - pdamage
                    print("You did ",pdamage," damage")
            else:
                print("NO")
        else:
            print("You died")
    else:
        print("Do you want to go back?")
        print("Yes")

