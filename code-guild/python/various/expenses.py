class Expense():
    def __init__(self):
	self.name = raw_input('expense name: ')
	self.amount = input('expense amaount: ')
	self.who_pays = raw_input('who pays?: ')
    
    category = None
    due_date = None		

    def update_name(self, Expense):
	Expense.name = raw_input('update expense name: ')
	return Expense
	
    def update_amount(self, Expense):
	Expense.amount = raw_input('update expense amount: ')
	return Expense

    def get_name(self, Expense):
	return Expense.name


class Month():
    def __init__(self):
	self.name = raw_input('which month is this?: ')

    monthly_expenses = {}

    def add_expense(self, Expense):
	self.monthly_expenses[Expense.name] = [Expense.name, Expense.amount, Expense.who_pays]
	return self.monthly_expenses

    def get_total_expenses(self):
	self.total = 0
	for k, v in self.monthly_expenses:
	    self.total += v[1]
	return self.total	

t = Month()

g = Expense()

t.add_expense(g)

#g.update_amount(g)

#g.due_date = '09/16/14'
#g.category = 'test'

#print(g.name)
#print(g.amount)
#print(g.who_pays)
#print(g.due_date)
#print(g.category)	
print(t.name)
print(t.monthly_expenses)
print(t.get_total_expenses())
