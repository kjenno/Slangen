import random


print("Welcome to the Overwatch Loot Box Simulator!")

OpenBox = input("Type 'open' to open a loot box!")

lijst = [
    'Legendary:',
    'Epic:',
    'Rare:',
    'Rare:',
    'Epic:',

]

if OpenBox == "open":
    print(random.choice(lijst))