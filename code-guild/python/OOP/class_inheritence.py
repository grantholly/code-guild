class Person(object):
    def __init__(self, name):
        self.name = name
        self.hobbies = []
        print("hi my name is " + self.name)

    def say(self, message):
        print(self.name + " says " + message)

    def work(self):
        print("let's get some work done!")

    def add_hobby(self, *hobbies):
        for hobby in hobbies:
            self.hobbies.append(hobby)
        return self.hobbies


class Programmer(Person):
    def __init__(self, name, *languages):
        super(Programmer, self).__init__(name)
        self.hobbies = ["programming"]
        self.languages = [lang for lang in languages]
        print("and I'm a programmer")

    def work(self):
        print("let's figure out a way that I never have to do that more than once")

    def say_langs(self):
        print("I can use " + " ".join(self.languages))


tim = Person("tim")
jess = Programmer("jess", "python", "javascript", "sql")

print(tim.name)
tim.add_hobby("fishing", "playing piano")
tim.say("i live in a program")
tim.work()

print(jess.name)
jess.add_hobby("calvin ball", "being 'indoorsy'")
jess.say("i too live in a program")
jess.work()
jess.say_langs()