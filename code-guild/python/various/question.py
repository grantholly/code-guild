questions = {1: ("what is your favorite color", "red, blue, green", "green"), 2: ("what is the average airspeed of the unladen swallow", "55km/hr, very fast, it is unknowable", "it is unknowable")}

def ask_question():
    for question in questions:
        print(questions[question][0])
        print(questions[question][1])
        response = raw_input("what is your answer?")
        if response == questions[question][2]:
            print("you got it right!")
        else:
            print("you got it wrong")

ask_question()
    
