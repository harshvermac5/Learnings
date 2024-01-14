old = ["a","b","a","c","a","d","b"]

#removes the duplicate without retaining order
new_01 = list(set(old))

#second approach that retains order
new_02 = []
for item in old:
    if item not in new_02:
        new_02.append(item)

#third approach that also retains order
new_03 = list(dict.fromkeys(old).keys())

print(new_01)
print(new_02)
print(new_03)