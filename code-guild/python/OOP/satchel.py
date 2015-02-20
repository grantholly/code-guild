class Character(object):
    def __init__(self, name):
        self.name = name
        self.attack = 10
        self.satchel = []
    
    def pick_up_item(self, item):
        self.satchel.append(item)

    def do_attack(self, item=False):
        if item:
            print(self.attack + item.damage)
        else:
            print(self.attack)

    def use_item(self):
        for item in self.satchel:
            print(item.name)
        user_choice = raw_input("pick an item")
        for item in self.satchel:
            if item.name == user_choice:
                self.do_attack(item)

class Item(object):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


hero = Character("grant")
rock = Item("rock", 10)
stick = Item("stick", 5)

hero.pick_up_item(rock)
hero.pick_up_item(stick)
hero.use_item()
