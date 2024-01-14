inv = [
    "gem",
    "sword",
    "shield",
    "potion",
    "coins"
]

#in case when you don't know the index
indx = inv.index("sword")
item = inv.pop(indx)

#insert at the last of list
inv.append(item)
print(inv)

#insert at specified place
inv.insert(3, item)
print(inv)