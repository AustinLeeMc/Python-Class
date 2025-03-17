print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, Which way do you want to go? Type "left" or "Right".').lower()

if choice1 == "left":
    choice2 = input('You\'ve come to a small lake and can see a figure upon the water. Type "wait" or "swim"').lower()

    if choice2 == "wait":
       choice3 = input("A small man arrives in a canoe and takes you to the island, upon the island are three doors."
              " red, yellow and blue."
              " Which color do you choose?").lower()
       if choice3 == "red":
           print("It's a room full of fire, Game Over.")
       elif choice3 == "yellow":
           print("You've found a room full of treasure! You win!")
       elif choice3 == "blue":
           print("It's a room full of beasts.. Game Over")
       else:
           print("This door doesn't exist, Game Over!")
    else:
        print("You were eaten by a shark, Game Over")

else:
    print("You fell into a hole. Game Over :( ")
