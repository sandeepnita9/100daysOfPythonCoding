print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("YOur mission is to find the treasure")
roadcross = input('YOu are at a crossroad, where do you want to go? Type "left" or "right"')
if roadcross.lower()=="right":
    print("Game Over")
else :
    swimORwait = input('You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "wsim" to swim across')
    if swimORwait.lower()=="swim":
        print("Game Over")
    else :
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. WHich colour do you choose?')
        if door.lower()=="red":
            print("Game Over")
        elif door.lower()=="blue":
            print("Game Over")
        else:
            print("COngratulations!!! You Won...")