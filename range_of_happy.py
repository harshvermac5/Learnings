x, y = int(input(f"Enter the number for finding Happy number from: ")), int(input(f"Enter the number for finding Happy number upto: "))

def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i)**2 for i in str(num))
    return num == 1

happy = []

for i in range(x, y+1):
    if is_happy(i) == True:
        happy.append(i)

print(f"Happy number between {x} and {y} are: \n {happy}")

#Happy number are those whose, sum of squares of its digits and same for it result ultimately leads to 1