import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("What will you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

print("Computer chose:")
print(game_images[computer_choice])
if user_choice < 0 or user_choice >= 3:
    print("Invalid choice, You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice < computer_choice:
    print("You lose!")
elif computer_choice < user_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("IT'S A DRAW!")