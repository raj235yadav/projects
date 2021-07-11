# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Snake Water Gun
import random

c1 = 0
p1 = 0
options = ["s", "w", "g"]

for i in range(10):
    computer = random.choice(options)
    player = input("Choose an option\n")
    if (player == "s") and (computer == "w"):
        p1 = p1+1
        print(computer)
    elif (player == "s") and (computer == "g"):
        c1 += 1
        print(computer)
    elif (player == "w") and (computer == "g"):
        p1 += 1
        print(computer)
    elif (player == "w") and (computer == "s"):
        c1 += 1
        print(computer)
    elif (player == "g") and (computer == "s"):
        p1 += 1
        print(computer)
    elif (player == "g") and (computer == "w"):
        c1 += 1
        print(computer)
    else:
        print(computer)
        continue
if c1 > p1:
    print(f"You Lost \n computer = {c1}, player = {p1}")
elif p1>c1:
    print(f"You Won \n player = {p1}, computer = {c1}")
else:
    print(f"Tied \n computer = {c1}, player = {p1}")