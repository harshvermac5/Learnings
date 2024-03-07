import random

max_lines = 3
max_bet = 100
min_bet = 1

rows = 3
cols = 3

symbol_count = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_value = {
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

def check_winnings(columns, lines, bet, values):


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(cloumns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(max_lines) + ")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <=lines <= max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        bet_amount = input("What would you like to bet? $")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if min_bet <= bet_amount <= max_bet:
                break
            else:
                print(f"Amount must be between {min_bet} and {max_bet}.")
        else:
            print("Please enter a number.")
    
    return bet_amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:

        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance:
            print(f"You don't have enough balance to bet that amount. You current balance is ${balance}.")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")
    print(balance, lines)

    slots = get_slot_machine_spin(rows, cols, symbol_count)
    print(slots)

main()