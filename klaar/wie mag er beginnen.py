import random
namen = []
D = int(input("Aantal spelers: "))
for B in range(D):
    B = input('naam: ')
    namen.append(B)
print(random.choice(namen))

