import random


class Hero(object):
    def __init__(self, energy):
        self.energy = energy


class Opponent(Hero):
    def __init__(self, energy):
        super(Opponent, self).__init__(energy)

def battle(hero, opponent):
    secret = str(random.randint(1, 3))
    guess = raw_input("guess a number")
    print(secret)
    if guess != secret:
        hero.energy -= opponent.energy
    else:
        print("you win")

teacher = Hero(3)
student = Opponent(1)

def main():
    def check_if_goat(hero):
        if hero.energy <= 0:
            print("you are now a goat")
            return False
    while True:
        battle(teacher, student)
        if check_if_goat(teacher) == False:
            break

main()
