#unordered, unique collection of iterable, mutuable elements represented in curly brackets
set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

union = set1|set2
subtraction = set1-set2
subtraction1 = set2-set1
intersection = set1&set2
differences = set1^set2

print(union)
print(subtraction)
print(subtraction1)
print(intersection)
print(differences)