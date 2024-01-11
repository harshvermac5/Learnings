n = int(input(f"Enter the number: "))
factorial = 1

if n < 0:
    print(f"No factorial for -ve numbers.")
elif n == 0:
    print(f"Factorial of 0 is 1")
else:
    for i in range(1, n+1):
        factorial = factorial*i
    print(f"The factorial of {n} is {factorial}")
