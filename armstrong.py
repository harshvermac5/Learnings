num = int(input("Enter a number: "))

# number of digits in the inserted number
num_str = str(num)
num_count = len(num_str)

sum_pwr = 0

for digit_str in num_str:
    digit = int(digit_str)
    sum_pwr += digit ** num_count

if sum_pwr == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

#Armstrong numbers are those whose sum of the values of each digit, raised to the power of the number's length, results in the original number.