import random

print("Coin Toss - Random Head or Tail Generator")
print("*****************************************")
#userInput = print("\n What you want HEAD or TAIL")
toss = random.randint(0,1)
if toss == 0:
    print("Tails")
else:
    print("Heads")