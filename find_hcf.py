def find_hcf(*numbers):
    if not numbers:
        return None

    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    result = numbers[0]

    for num in numbers[1:]:
        result = gcd(result, num)

    return result

# Ask the user how many numbers they want to find the HCF for
num_count = int(input("Enter the number of numbers for HCF: "))

# Get input for each number
numbers = []
for i in range(num_count):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

# Find the HCF of the provided numbers
result = find_hcf(*numbers)

print(f"The HCF is {result}")
