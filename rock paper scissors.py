from random import randint, choice

possibility= ['rock', 'paper', 'scissors']
comp = choice(possibility)
computer = randint(possibility)
def get_winner(computer ,p1):
    if computer == p1:
         return "TIE" 
    elif computer == "rock":
        if p1 == "scissors":
           return "computer wins"
        
        else:
              return "player wins"
              
    elif computer == "paper":
        if p1 == "rock":
            return "computer wins"
            
        else:
                return "player wins"
    elif computer == "scissors":
        if p1 == "paper":
            return "computer wins"
        else:
                return "player wins"
    else:
        return "Invalid Input"            
p1 = input("player. rock paper scissors: ")
print(get_winner(computer, p1))


