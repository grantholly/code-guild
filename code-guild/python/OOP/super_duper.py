class Parent(object):
    def m(self):
        return "parent called"

# call the previously defined version of a method in a parent class
class Child(Parent):
    def m(self):
        print("calling m from Child")
        return super(Child, self).m()


class Parent(object):
    def __init__(self, x):
        self.x = x

# call the parent class __init__ to send init arguments up into a parent class
# and have htem cascade back down through inheritence
class Child(Parent):
    def __init__(self, x, y):
        print("calling the __init__ in Parent")
        super(Child, self).__init__(x)
        self.y = y


class Parent(object):
    def m(self):
        return "parent m called"


# make an explicit call to the parent class method
class Child(Parent):
    def m(self):
        return Parent.m()

# Stick to either using super or parent class method calls.  
# Mixing the two can be very confusing

