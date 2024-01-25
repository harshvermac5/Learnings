list_01 = [
    "Torch",
    "Rock",
    "Sword",
    "Shield"
]

#.index method is useful in case when we don't know the index position of the element
index = list_01.index("Sword")
item = list_01.pop(index)
list_01.insert(0, item)

print(list_01)