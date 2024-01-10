x = [1,2,3,1,3,5,4,6,5,6,6,3,2,7]

most_01 = max(x) #finds the largest value
most_02 = max(x, key=x.count) #finds the most repeated value
most_03 = max(set(x), key=x.count) #making the above code more efficient


print(most_01)
print(most_02)
print(most_03)