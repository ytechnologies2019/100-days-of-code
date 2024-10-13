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

# Display choices to the user
print("Choose: 1 for Rock, 2 for Paper, 3 for Scissors")
user_input = int(input("Enter your choice (1/2/3): "))

if user_input == 1:
    print("You chose Rock:")
    print(rock)
elif user_input == 2:
    print("You chose Paper:")
    print(paper)
elif user_input == 3:
    print("You chose Scissors:")
    print(scissors)
else:
    print("Your output is wrong.")
    exit()  # Exit if the input is invalid

# Computer choice
computer_choice = random.choice([1, 2, 3])
if computer_choice == 1:
    print("Computer chose Rock:")
    print(rock)
elif computer_choice == 2:
    print("Computer chose Paper:")
    print(paper)
elif computer_choice == 3:
    print("Computer chose Scissors:")
    print(scissors)

# Determine the result
if user_input == computer_choice:
    print("It's a draw!")
elif (user_input == 1 and computer_choice == 3) or (user_input == 2 and computer_choice == 1) or (user_input == 3 and computer_choice == 2):
    print("You win!")
else:
    print("You lose!")
