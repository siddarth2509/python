import random

class game:
    def __init__(self,rounds):
        self.l3 = ["stone","paper","scissors"]
        self.playerscores = 0
        self.computerscore = 0
     
        for i in range(rounds):
            a = random.choice(self.l3)
            chce = input("enter the choice:")
            if chce == a:
                print("its a tie")
            elif chce == "stone" and a == "paper" or chce == "paper" and a == "scissors" or chce == "scissors" and a == "stone":
                print("computer wins")
                self.computerscore += 1
            else:
                print("you won")
                self.playerscores += 1
        
    def output(self):
        print("you: ",self.playerscores, "computer: ", self.computerscore)   
        if self.playerscores > self.computerscore:
            print("You wins")
        else:
            if self.playerscores < self.computerscore:
                print("You lose")
            else:
                print("its a tie")  
rounds = int(input("enter the number of rounds"))
p1 = game(rounds)
p1.output()

    