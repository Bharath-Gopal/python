#Rock, Paper, Scissors
import random 

print("\n")
print("-"*50)
print("Rock, Paper, Scissors")
print("-"*50)
print("\n")

while True:
    print("Pick your choice : ")
    print("1. Rock\n2. Paper\n3. Scissors\n")
    choice = int(input())

    if choice==1:
        cn="Rock"
    elif choice==2:
        cn="Paper"
    elif choice==3:
        cn="Scissors"
    else :
        print("INVALID CHOICE")
        break

    print("User's Choice : ",cn)

    c_choice = random.randint(1,3)
    if c_choice==1:
        ccn="Rock"
    elif c_choice==2:
        ccn="Paper"
    else:
        ccn="Scissors"

    print("Computer's Choice : ",ccn)

    if ((choice==1 and c_choice==3) or (choice==3 and c_choice==1)):
        print("Rock Wins!")
        result = "Rock"
    elif ((choice==1 and c_choice==2) or (choice==2 and c_choice==1)):
        print("Paper Wins!")
        result = "Paper"
    elif ((choice==1 and c_choice==1) or (choice==1 and c_choice==1)):
        print("Draw!")
        result = "Rock"
    elif ((choice==2 and c_choice==3) or (choice==3 and c_choice==2)):
        print("Scissors Wins!")
        result = "Scissors"
    elif ((choice==2 and c_choice==2) or (choice==2 and c_choice==2)):
        print("Draw!")
        result = "Paper"
    else:
        print("Draw!")
        result = "Scissors"

    if(result == cn):
        print("USER WINS!!!")
    elif(result == ccn):
        print("COMPUTER WINS!!!")
    else:
        print("DRAW")

    print("Do you want to play again? (Y/N)")
    ans = input()

    if(ans == 'n' or ans == 'N'):
        break

print("\nThanks for Playing\n")
