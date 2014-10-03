def check_computer_hand(x):
    for i in [2, 17, 42, 38, 28]:
	if i % 13 == x:
	    return i
	

def ask_for_card(c):
    keys = range(1, 14)
    nums = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']
    words = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
    
    for i, j, k in zip(keys, nums, words):
	if c in (j, k):
	    c = i
	    check_computer_hand(c)
	    print(c)
	    #return c

ask_for_card('k')

