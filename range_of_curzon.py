def curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

curzon_upto = int(input(f"Find the curzon number upto: "))

curzon_list = []

for num in range(curzon_upto + 1):
    if curzon(num):
        curzon_list.append(num)
print(curzon_list)