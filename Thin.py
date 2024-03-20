class player():
    def __init__(self):
        self.health = 100
        self.attack = 3
        self.defense = 1
        self.attackboost = 0
        self.defenseboost = 0
        self.regen = 1
        self.gold = 0

p = player()

def Hub():
    def Shop(): # For buying equipment with gold
        pass
    def Blacksmith(): # For upgrading equipment with gold
        pass
    def TravelCart(): # Going to fight enemies
        pass
    Go = input("Where in town go? \n Shop(1) \n Blacksmith(2) \n Travel Cart(3)")
    if Go == "1":
        Shop()
    elif Go == "2":
        Blacksmith()
    elif Go == "3":
        TravelCart()
    else:
        print("You exit because you bad")
        exit()
