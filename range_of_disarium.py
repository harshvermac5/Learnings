x, y = int(input(f"Disarium from: ")), int(input(f"Disarium upto: "))

def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i)**(index+1) for index, i in enumerate(num_str))
    return digit_sum == number

disarium = []

for i in range(x, y+1):
    if is_disarium(i) == True:
        disarium.append(i)

print(f"Disarium number are: \n {disarium}")