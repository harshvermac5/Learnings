#input the number to be checked
n = int(input("Enter a number: "))

m = (n % i != 0 for i in range(2, int(n**0.5)+1))

print(m)
"""
#check if the number is prime
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")"""
