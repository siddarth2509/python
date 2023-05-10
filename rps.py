import random
rounds = int(input("enter the no of rounds to play the game"))
l3 = ["stone","paper","scissors"]
playerscores = 0
computerscore = 0
for i in range(rounds):
    a = random.choice(l3)
    chce = input("enter the choice:")
    if chce == a:
        print("its a tie")
    elif chce == "stone" and a == "paper" or chce == "paper" and a == "scissors" or chce == "scissors" and a == "stone":
        print("computer wins")
        computerscore += 1
    else:
        print("you won")
        playerscores += 1
print("you: ",playerscores, "computer: ", computerscore)   
if playerscores > computerscore:
    print("You wins")
else:
    if playerscores < computerscore:
        print("You lose")
    else:
        print("its a tie")  
    