import random

# asking the user for the maximum number in range
top_of_range = input("Type a number: ")

# confirming whether the input is valid number or not
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()

else:
    # printing the statement
    print("Please type a number next time.")
    quit()

# selecting a number 
random_number = random.randint(0, top_of_range)

guesses = 0

while True:
    guesses += 1

    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        if user_guess < random_number:
            print("You are below the number.")
        elif user_guess > random_number: # This line was changed
            print("You are above the number.")

print(f"You got it in {guesses} guesses.")