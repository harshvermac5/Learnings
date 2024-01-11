#09

#getting values from the terminal
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

#calculating discriminant
discriminant = b**2 - 4*a*c

#applying conditions if the discriminant is +ve, -ve or zero
if discriminant > 0:
    root1 = (-b + (discriminant**0.5)) / (2*a)
    root2 = (-b - (discriminant**0.5)) / (2*a)
    print(f"Root 1 is {root1}")
    print(f"Root 2 is {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"The only real root is {root}")
else:
    real_part = -b / (2*a)
    imaginary_part = ((abs(discriminant)**0.5)/(2*a))
    print(f"Root 1 is {real_part} + {imaginary_part}i")
    print(f"Root 2 is {real_part} - {imaginary_part}i")