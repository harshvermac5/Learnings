import random
import time

operators = ["+", "-", "*"]
min_operand = 3
max_operand = 12
total_problems = 10

# function to generate problems
def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    # eval evaluates the mathematical expression, even after it is string data type
    answer = eval(expr)
    return expr, answer

# using decorator to beautify the program
def my_decorator(func):
    def wrapper():
        input("Press enter to start! ")
        print("--------------------------")
        start_time = time.time()
        func()
        end_time = time.time()
        total_time = end_time - start_time
        print("--------------------------")
        print(f"Nice Work! You finished in, {total_time}, seconds!")
    return wrapper

# applying the decorator on the main function
@my_decorator
def ask_problem():
    for i in range(total_problems):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i+1) + ": " + expr + " = ")
            if guess == str(answer):
                break

ask_problem()
