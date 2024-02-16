# Define a function to check if a number is even
def is_even(x):
    return x % 2 == 0

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter() to select only the even numbers from the list
#in short, Filter checks the list after a function, and returns only the values in the list that hold true for the function
even_numbers = filter(is_even, numbers)

#Use map to check the number whether they are even or not
#in short, Map runs the same function over a list and returns the result (Boolean in this case)
check_even = map(is_even, numbers)

# Convert the iterator to a list to see the results
print(list(even_numbers))
print(list(check_even))

