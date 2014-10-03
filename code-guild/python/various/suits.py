suits = ["hearts", "diamonds", "clubs", "spades"]
numbers = range(2, 11)
faces = ["jack", "queen", "king", "ace"]
cards = []
deck_of_cards = {}

for suit in suits:
    for number in numbers:
	cards.append(str(number) + " of " + suit)
    for face in faces:
	cards.append(face + " of " + suit)	

#print(cards)

for i in range(1, 53):
    deck_of_cards[i] = cards[i - 1]

print(deck_of_cards)


