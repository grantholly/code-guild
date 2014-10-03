import random


class Sea():
    def __init__(self, name):
        self.name = name
        self.weather = 'cool and calm'
        self.ships = []

        for ship in self.ships:
            print("{} is sailing on the {}".format(ship.name, self.name))


class Ship():
    def __init__(self, name, sails, cannons):
        self.name = name
        self.sails = sails
        self.cannons = cannons
        self.sailors = []

    def sail(self):
        print("off we go")

    def conscript_sailors(self, *sailors):
        for sailor in sailors:
            self.sailors.append(sailor)

    def full_broadside(self, target):
        print("fire a full broadside at {}".format(target.name))


class Sailor():
    def __init__(self, name, ship):
        self.name = name
        self.ship = ship
        self.sweetheart = None

    def swim(self):
        print("I'm overboard")

    def set_sail(self):
        return ship.sail()


class Pirate(Sailor):
    def __init__(self, name, ship):
        Sailor.__init__(self, name=name, ship=ship)
        self.pegleg = True
        self.weapon = 'sword'
        self.drink = ''
        self.BAL = "yaaar"

    def pirate_speak(self):
        shanty = raw_input("who be thar?")
        print("yar har " + shanty)


class RoyalNavySailor(Sailor):
    def __init__(self, name, ship):
        Sailor.__init__(name=name, ship=ship)
        self.salary = 50

    def eat_lime(self):
        print("no scurvy for me")

    def walk_the_plank(self, criminal_scum):
        print("walk the plank {}, you pirate scum".format(criminal_scum.name))


class HighSea(Sea):
    def __init__(self, name, sea):
        Sea.__init__(self, name=name)
        self.sea = sea

    def storm(self):
        Sea.ships.pop(random.choice(Sea.ships))

    def RELEASE_THE_KRAKKEN(self):
        for ship in Sea.ships:
            Sea.ships.remove(ship)
        print("We've been destroyed by the mythical Krakken")


def main():
    indian_ocean = Sea("Indian Ocean")
    gulf_of_aden = HighSea("Gulf of Aden", indian_ocean)

    man_o_war = Ship("man of war", sails=20, cannons=15)

    cerberus = Ship("cerberus", sails=20, cannons=10)

    black_pearl = Ship("black pearl", sails=25, cannons=10)
    black_pearl.treasure_map = "follow the dotted line to the X"

    gulf_of_aden.ships = [man_o_war, cerberus, black_pearl]

    carl = Sailor("Carl", man_o_war)
    carl.sweetheart = "Tawny"

    mick = Sailor("Mick", cerberus)
    mick.weapon = "blunderbuss"

    man_o_war.conscript_sailors(carl, mick)

    jack = Pirate("Jack", black_pearl)
    jack.sweetheart = "Tawny"
    jack.drink = "bottle of rum"

main()









