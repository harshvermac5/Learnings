inv = {
    "Sword":1,
    "Potion":2
}

loot = {
    "Sword":3,
    "Potion":4,
    "Sheild":5
}

#to update the old dict with new values
inv.update(loot)

#to add up to the old values
new_inv = {
    k: inv.get(k,0) + loot.get(k,0) \
   for k in set(inv | loot)
}

print(new_inv)

#another approach to solve above problem
for key in loot:
    inv[key] = inv.get(key,0)  + loot[key]

print(inv)