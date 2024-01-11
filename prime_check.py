#input the number to be checked
n = int(input("Enter a number: "))

#If the remainder is not equal to zero for all the numbers in the range,
#then the input number is a prime number and the value of m will be True
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5)+1)):
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")