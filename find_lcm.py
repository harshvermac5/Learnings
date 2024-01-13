def find_lcm(*numbers):
    if not numbers:
        return None
    
    #using euclidean algorithm to find Greatest common divisor
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    #finding lcm by diving the product of numbers by its Greatest common divisor
    def lcm(x, y):
        return x * y // gcd(x, y)
    
    #initialising an empty list
    result = numbers[0]

    #using recursion for every digit in values
    for num in numbers[1:]:
        result = lcm(result, num)

    return result

# Ask the user how many numbers they want to find the LCM for
num_count = int(input("Enter the number of numbers for LCM: "))

# Get input for each number
numbers = []
for i in range(num_count):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find the LCM of the provided numbers
result = find_lcm(*numbers)

print(f"The LCM is {result}")
