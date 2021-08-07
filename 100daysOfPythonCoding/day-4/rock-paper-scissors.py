import random
print("Welcome to Game of Rock, Paper & Scissors")
print("*****************************************")
# Rock Paper Scissors ASCII Art

# Rock
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Paper
paper = '''
PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Type \n 0 for ROCK \n 1 for Paper \n 2 for Scissor")
userChoice = int(input("ENter yur choice"))
if userChoice < 0 or userChoice > 2:
    print("You have entered incorrect choice. Try Again")
    exit()
else :
    computerChoice = random.choice([0,1,2])
    rockpaperscissorsList = [rock, paper, scissors]
    print("You Selected \n")
    print(rockpaperscissorsList[userChoice])
    print("\n \n")
    print("\n Computer Selected")
    print(rockpaperscissorsList[computerChoice])

    if computerChoice == 0 and userChoice == 0:
        print("Draw")
    elif computerChoice == 0 and userChoice == 1:
        print("You WON")
    elif computerChoice == 0 and userChoice == 2:
        print("Computer WON")
    elif computerChoice == 1 and userChoice == 0:
        print("Computer Won")
    elif computerChoice == 1 and userChoice == 1:
        print("Draw")
    elif computerChoice == 1 and userChoice == 2:
        print("You Won")
    elif computerChoice == 2 and userChoice == 0:
        print("You Won")
    elif computerChoice == 2 and userChoice == 1:
        print("Computer Won")
    elif computerChoice == 2 and userChoice == 2:
        print("Draw")
    else:
        print("Something wrong. Please try again")
