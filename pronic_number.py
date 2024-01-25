#Number which can be represented as multiple with its consecutive terms

def is_pronic(num):
    for n in range(1, int(num**0.5)+1):
        if n * (n+1) == num:
            return True
    return False
        
ent = int(input("Enter the number to check: "))

if is_pronic(ent):
    print(f"Yes, {ent} is Pronic.")
else:
    print(f"Nope, {ent} is not Pronic.")
