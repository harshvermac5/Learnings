import random

user_wins = 0
computer_wins = 0

print("This is Rock paper Scissor game.")
print("I WELCOME YOU here.")

options = ["r", "p", "s", "t"]

while True:
    user_input = input("Type R, P, S, or Q for Rock, Paper, Scissors, or Quit respectively: ").lower()
    
    if user_input == "q":
        break
    
    if user_input not in ["r", "p", "s"]:
        print("Invalid input. Please enter R, P, S, or Q.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]

    print(f"Computer picked {computer_pick}.")

    if (user_input == "r" and computer_pick == "s") or \
       (user_input == "p" and computer_pick == "r") or \
       (user_input == "s" and computer_pick == "p"):
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You Lost!")
        computer_wins += 1

print(f"You won {user_wins} times.")
print(f"The Computer won {computer_wins} times.")
print("Adios!")

print("I Love You, Thank Youu For using it.")