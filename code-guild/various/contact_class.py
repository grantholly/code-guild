class Contact():
    def __init__(self, name, number):
	self.name = name
	self.number = number

    def new_contact(self):
	prompt1 = raw_input('enter the name')
	prompt2 = input('enter the number')
	added_contact = Contact(prompt1, prompt2)
	print added_contact
	return added_contact

kala = Contact('kala', 12345)
print(kala.name, kala.number)
mala = Contact('mala', 1)
print(mala.name, mala.number)
mala.new_contact()
