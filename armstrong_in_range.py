def is_armstrong_number(num):
    # Calculate the number of digits
    num_str = str(num)
    num_digits = len(num_str)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    # Check if the sum is equal to the original number
    return armstrong_sum == num

def find_armstrong_numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

# Define the range
start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

# Find Armstrong numbers within the defined range
result = find_armstrong_numbers(start_range, end_range)

# Display the result
print(f"Armstrong numbers between {start_range} and {end_range}: {result}")
