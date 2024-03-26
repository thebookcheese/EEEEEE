import random

def Drop1(p, Min, Max):
    Bonus = random.randint(Min,Max)
    print("You found a sword which gives +",Bonus," attack")
    Equip = input("Do you want to equip Y/N").lower()
    if Equip == "y":
        p.attackboost = p.attackboost + Bonus
        print("Your attack bonus is +",p.attackboost)
    else:
        print("OK")

def Drop2(p, Min, Max):
    Bonus = random.randint(Min,Max)
    print("You found a shield which gives +",Bonus," defense")
    Equip = input("Do you want to equip Y/N").lower()
    if Equip == "y":
        p.defenseboost = p.defenseboost + Bonus
        print("Your defense bonus is +",p.defenseboost)
    else:
        print("OK")


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
            Do = input("What do you want to do? \n Attack (1) \n Exit (2)")
            if Do == "1":
                SDamage = SAtt - (p.defense + p.defenseboost)
                Dodge = random.randint(1,100)
                if Dodge < (p.dodge + 1):
                    print("Player dodged")
                else:
                    p.health = p.health - SDamage
                    print("You took ",SDamage," damage")
                    print("You are now on ",p.health," health")
                pdamage = (p.attack + p.attackboost) - SDef
                if Dodge < (SDodge + 1):
                    print("Slime dodged")
                else:
                    SHP = SHP - pdamage
                    print("You did ",pdamage," damage")
                    print("The slime is on ",SHP," health")
            elif Do == "2":
                exit()
            else:
                print("NO")
        else:
            print("You died")
    else:
        Loot = random.randint(1,2)
        if Loot == 1:
            Drop1(p,1,3)
        else:
            Drop2(p,1,3)
        GoldGain = random.randint(3,10)
        p.gold = p.gold + GoldGain
        print("Yoou gained ",GoldGain," gold from the slime. You now have ",p.gold," gold")
        
        print("Do you want to go back?")
        print("Yes")

