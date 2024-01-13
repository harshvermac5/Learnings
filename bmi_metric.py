def bodymassindex(height, weight):
    return round((weight/height**2), 2)

h = float(input(f"Enter your height in meters: "))
w = float(input(f"Enter your weight in kilograms: "))

bmi = bodymassindex(h, w)
print(f"Your BMI is: {bmi}")

if bmi <= 18.5:
    print("You're Underweight.")
elif 18.5 < bmi <= 24.9:
    print("Your weight is normal.")
elif 25 < bmi <= 29.29:
    print("You are overweight.")
else:
    print("You are obese.")

