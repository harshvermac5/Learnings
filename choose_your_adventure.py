name = input("Type your name: ")

print(f"Welcome {name} to the adventure!")

answer = input("You are on dirt road, it has come to an end and you can go left or right: ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk along or build a raft")

elif answer == "right":
    answer = input("You come to a")

else:
    print("Not a valid Input")