def new_game():
    guesses=[]
    # correct_guesses=0
    question_number=1
    for key in questions:
        print(key)
        for i in options[question_number-1]:
            print(i)
        guess= input("Enter (A,B):")
        guess= guess.upper()
        guesses.append(guess)
        print(check_answer(questions,guess))
        play_again()
        # break
    correct_guesses += check_answer(questions.get(key),guess)
    question_number += 1

def check_answer(questions,guess):
    for i in questions:
        # print(i)
        if questions[i]==guess:
            print("CORRECT:")
            # return 1
        else:
            print("WRONG:")
            # return 0
            break
    
def play_again():

    response = input("Do you want to play again? (Yes or No): ")
    response = response.upper()


    if response == "Yes":
        return True
    else:
        return False
# start=input("do you play game")
# if start == "yes":
#     print("yes")
# else:
#     print("no")
questions={"what is API?: ": "A",
"what is ACL?: ": "A",
"what is BGP?: ": "A",
"what is CLI?: ": "B",
"what is CPU?: ": "B",
"what is DMI?: ": "A",
"what is FTI?: ": "A",
"what is Gbps?: ": "B",
"what is HTTP: ": "A",
"what is HTTPS?: ": "A"}

options=[["A.Application Programing Interface","B.Appliction Programing Interpeter"],
["A.Access Control List","B.Access Conterol Set"],
["A.Border Gateway Protocol","B.Border Gateway Protel"],
["A.Commend line Interface","B.Commend line Interpretr"],
["A.Central Proccessing Per","B.Central Proccessing Unit"],
["A.Desktop Management Interface","B.Desktop Management"],
["A.File Transfer Protocol","B.File Transfer Portable"],
["A.gigabit per menite","B.gigabit per second"],
["A.HyperText Transfer Protocol","B.Nothig"],
["A.HyperText Transfer protocol Secure","B.Wrong"]]


start=input("do you want to play game")
if start == "yes":
    print("yes")
    new_game()
else:
    print("no")
# new_game()

while play_again():
    new_game()
new_game()

play_again()

print("Bye")