def is_harshad(num):
    str_num = str(num)
    num_list = [int(i) for i in str_num]  # Convert each digit to an integer
    if num % sum(num_list) == 0:
        return True
    return False

harshad = []

x,y = int(input("Enter the number from which you want to check for Harshad Number: ")), int(input("Enter the number upto which you want to check for Harshad Number: "))

for i in range(x, y+1):
    if is_harshad(i) == True:
        harshad.append(i)

print(f"Harshad number between the range {x} and {y} are: \n {harshad}")