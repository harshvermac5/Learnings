def curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0

print(curzon(5))
print(curzon(10))
print(curzon(15))