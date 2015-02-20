class Hero(object):
    def __init__(self, name):
        self.name = name
        self.points = 100
    
    def attack(self, monster):
        monster.points -= 10
    
    def defend(self):
        self.points += 10


class Monster(object):
    def __init__(self, name):
        self.name = name
        self.points = 50

    def attack(self, hero):
        print("oh no you have been attacked by " + self.name)

    def shreek(self):
        print("EEEAAAAKKKK!")


class Battle(object):
    def __init__(self, hero, monster):
        self.hero = hero
        self.monster = monster

    def fight(self):
        while self.hero.points > 0 and self.monster.points > 0:
            self.monster.attack(self.hero)
            action = raw_input("attack or defend?")
            if action == "attack":
                self.hero.attack(self.monster)
            if action == "defend":
                self.hero.defend()

def main():
    user_name = raw_input("what is your hero name?")
    player = Hero(user_name)

    monster = Monster("Mummy")

    the_fight = Battle(player, monster)
    the_fight.fight()

main()
