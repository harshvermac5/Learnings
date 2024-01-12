nterms = int(input(f"How many terms? "))
#First two terms
n1, n2 = 0, 1
count = 0

if nterms <= 0:
    print(f"Fibonnaci exist for a positive number only")
elif nterms == 1:
    print(f"Fibonnaci sequence upto {nterms} are: ")
    print(n1)
else:
    print(f"Fibonacci sequence upto {nterms} are: ")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

    