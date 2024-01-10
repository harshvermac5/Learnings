list_01 = [
    "Torch",
    "Rock",
    "Sword",
    "Shield"
]

index = list_01.index("Sword")
item = list_01.pop(index)
list_01.insert(0, item)

print(list_01)