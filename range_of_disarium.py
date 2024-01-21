x, y = int(input(f"Disarium from: ")), int(input(f"Disarium upto: "))

def is_disarium(number):
    num_str = str(number)
    #index + 1 is the position, while i is the element
    digit_sum = sum(int(i)**(index+1) for index, i in enumerate(num_str))
    return digit_sum == number

disarium = []

for i in range(x, y+1):
    if is_disarium(i) == True:
        disarium.append(i)

print(f"Disarium number are: \n {disarium}")

#Disarium number are those whose sum of digits rose to the power of their position from left, equals to the digit itself.