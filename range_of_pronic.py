def is_pronic(num):
    for n in range(1, int(num**0.5)+1):
        if n * (n+1) == num:
            return True
    return False

x, y = int(input("Enter the number from you want to find Pronic: ")), int(input("Enter the number upto you want to find Pronic: "))

pronic = []

for i in range(x, y+1):
    if is_pronic(i):
        pronic.append(i)
print(f"Pronic number inside the range {x}, and {y} are: {pronic}")