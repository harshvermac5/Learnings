#Happy number is a positive integer that ultimately reaches the value of 1, if you keep doing the sum of square of its digits and of its result.

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i)**2 for i in str(num))
    return num == 1

num = int(input("Enter the number you want to test: "))
if is_happy(num):
    print(f"{num} is a Happy number.")
else:
    print(f"{num} is not a Happy number.")
