def reverse(input_str):
    reversed_str = input_str[::-1].swapcase()
    return reversed_str

input_01 = input(f"Input the String you want to reverse. ")

print(reverse(input_01))