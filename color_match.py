import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 6
CODE_LENGTH = 4

# generates the secret code with items of the above list
def generate_code():
    code = {}

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

# formatting the input and comparing it with the allowed color list
def guess_code():
    while True:
        guess = input("Guess: ").upper()

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        # all returns true if the condition of checking color in both the list holds true
        if not all(color in COLORS for color in guess):
            print("Invalid colors. Valid colors are:", *COLORS)
            continue
        
        break

    return list(guess)

# comparing the user input with the secret code, incrementing the desired counter
def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_count[guess_color] -= 1

    for guess_color in guess:
        if guess_color in real_code and color_count[guess_color] > 0:
            incorrect_pos += 1
            color_count[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome to the Mastermind, you have {TRIES} tries to guess the code...")
    print("The valid colors are:", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES+1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries.")
            break

        print(f"Correct position: {correct_pos} | Incorrect position: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was:", *code)

if __name__ == "__main__":
    game()
