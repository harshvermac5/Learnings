def is_harshad(num):
    str_num = str(num)
    num_list = [int(i) for i in str_num]  # Convert each digit to an integer
    if num % sum(num_list) == 0:
        return True
    return False

check = int(input("Enter the number to check: "))

if is_harshad(check):
    print(f"{check} is a Harshad number.")
else:
    print(f"{check} is not a Harshad number.")

#harshad number are that who is divisible by the sum of its digit