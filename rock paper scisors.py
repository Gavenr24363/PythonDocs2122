Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____) ROCK BEATS SCISSORS
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______) PAPER BEATS ROCK
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________) SCISSORS BEAT PAPER
      (____)
---.__(___)
'''
while True:
    game_images = [rock, paper, scissors]

    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice > user_choice):
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
