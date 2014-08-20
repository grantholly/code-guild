__author__ = 'grant'

secret = input("type your secret word here").lower()
word = ['X' for i in secret]
guessedletters = []
print(word)

def makeguess():
    guess = input("guess a letter").lower()
    checkguess(guess)
    print("you have guessed")
    print(guessedletters)
    if guess in secret:
        findreplace(guess)
        print(word)
    else:
        print("you guessed wrong")
    guessedletters.append(guess)

def checkguess(guess):
    if guess in guessedletters:
        print("you already guessed that one")
        makeguess()
    elif not guess.isalpha():
        print("you can only use letters")
        makeguess()
    else:
        pass

def findreplace(guess):
    for i, x in enumerate(secret):
        if guess == x:
            word[i] = x
    print("good job")
    return word
    makeguess()

def main():
    tries = 13
    while tries:
        print("you have" + " " + str(tries) + " " + "tries")
        makeguess()
        tries += 1
        if word == list(secret):
            print("you did it")
            break
        tries -= 1
    print("too bad")

main()