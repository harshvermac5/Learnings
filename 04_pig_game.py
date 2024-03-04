import random

# Function to simulate rolling a dice
def roll():
    min_val = 1
    max_val = 6
    roll_result = random.randint(min_val, max_val)
    return roll_result

# Prompting the user to input the number of players
while True:
    players = input("Enter the number of players: ")
    # Validating if the input is a digit
    if players.isdigit():
        players = int(players)
        # Validating if the number of players is between 2 and 4
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 Players.")
    else:    
        print("Invalid, try again.")

max_score = 50
player_score = [0 for _ in range(players)]

# Main game loop continues until a player reaches the max_score
while max(player_score) < max_score:

    # Iterating through each player's turn
    for player_idx in range(players):
        print(f"\nPlayer number {player_idx + 1}'s turn has just started!\n")
        current_score = 0

        # Loop for each player's turn
        while True:

            should_roll = input("Would you like to roll? (y/n) ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn Finished.")
            else:
                print(f"You rolled a {value}!")
                current_score += value  # Accumulating the score for each roll
            print(f"Your score is {current_score}")
        
        player_score[player_idx] += current_score
        print(f"Your total score is {player_score[player_idx]}")

# Determining the winner
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f"Player number {winning_idx + 1} is the winner with a score of {max_score}")
