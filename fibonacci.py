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
        #Temporary variable to store next iteration
        nth = n1 + n2
        #Transferring the values to complete the sequence
        n1 = n2
        n2 = nth
        #incrementing the counter
        count += 1