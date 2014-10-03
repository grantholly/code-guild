class Contact():
    def __init__(self, name, number):
	self.name = name
	self.number = number

d = Contact('david', 8888)

class Directory():
    def __init__(self):
	self.contact_dict = {}

    def add_entry(self, Contact):
	self.contact_dict[Contact.name] = [Contact.name, Contact.number]
	return self.contact_dict

    def edit_number(self, Contact):
	self.user_prompt = raw_input('who do you want to edit?: ')
	self.change = input('change their number to: ')
	self.contact_dict[self.user_prompt][1] = self.change
	return Contact

phonebook = Directory()

phonebook.add_entry(d)

phonebook.edit_number(d)

print(phonebook.contact_dict)

{'david': ['david', 9999]}
