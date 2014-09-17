class User():
    def __init__(self, firstname, lastname, email, city, state):
	self.firstname = firstname
	self.lastname = lastname
	self.fullname = self.firstname + " " + self.lastname
	self.email = email
	self.city = city
	self.state = state

        self.age = None
        self.ethnicity = None
        self.occupation = None
        self.hobbies = []

    def save_user(self, User):
	self.user_state = {}
	self.user_state[self.fullname] = {'age': self.age, 'first name': self.firstname}
	return self.user_state

q = User(firstname='grant', lastname='holly', email='grant@grant.com', city='Portland', state='OR')
q.age = 29
q.save_user(q)

print(q.firstname, q.age, q.user_state)
    
