import random
import string

def generate_password(min_length, numbers=True, special_char=True):
    # assigning variable to various string modules
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    # if the parameters are True for numbers and special_char, only that our character variable is loaded with the desired characters
    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    # creating an empty string, to be filled until all the criterias met
    pwd = ""
    # setting the initial criterias False
    meets_criteria = False
    has_number = False
    has_special = False

    # creating a while loop, continuting until criterias are met
    while not meets_criteria or len(pwd) < min_length: # not meet criteria is to counteract the inital values
        new_char = random.choice(characters)
        pwd += new_char

        # setting the respected flag to true, if the newly added character pass the test
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        # assuming the default criteria as True, then checking against the respected variable
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_char:
            meets_criteria = meets_criteria and has_special
    
    return pwd

min_length = int(input("Enter the Minimum length: "))
has_number = input("Do you want to have number? (y/n) ").lower() == "y" # equating with y turns string into boolean
has_special = input("Do you want to have special character (y/n) ").lower() == "y" # equating with y turns string into boolean
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is {pwd}")