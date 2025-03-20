import random


dice1 = r'''

   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
   '''

dice2 = r'''

                                       _______.
                            ______    | .   . |\
                           /     /\   |   .   |.\
                          /  '  /  \  | .   . |.'|
                         /_____/. . \ |_______|.'|
                         \ . . \    /  \ ' .   \'|
                          \ . . \  /    \____'__\|
                           \_____\/
'''

dice3 = r'''

                                     ____
                                    /\' .\    _____
                                   /: \___\  / .  /\
                                   \' / . / /____/..\
                                    \/___/  \'  '\  /
                                             \'__'\/ 
'''

game_images = [dice1, dice2, dice3]


input("Welcome to the table, Have what it takes? Type Roll\n").lower()
roll = random.randint(1,6)
print(roll)
print(random.choice(game_images))
computer_choice = random.randint(1,6)
print(computer_choice)
print(random.choice(game_images))
if roll < computer_choice:
    print("You lose!")
elif computer_choice < roll:
    print("You win!")
elif roll == computer_choice:
    print("Draw! Roll again")

input("Redemption roll\n").lower()
roll = random.randint(1,3)
print(roll)
print(random.choice(game_images))
computer_choice = random.randint(1,3)
print(computer_choice)
print(random.choice(game_images))
if roll < computer_choice:
    print("You lose!")
elif computer_choice < roll:
    print("You win!")



















