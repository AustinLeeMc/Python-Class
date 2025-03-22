import random
from hangman_words import word_list
from hangman_art import stages, logo
lives = 6
game_over = False
chosen_word = random.choice(word_list)

print(logo)
print(chosen_word)
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

correct_letters = []

while not game_over:
    guess = input("Guess a letter ").lower()
    if guess in correct_letters:
        print("You've already chose that one!")
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You're man has hung, Game Over!")
            print(f"The word you were looking for was {chosen_word}! ")
    print(stages[lives])



