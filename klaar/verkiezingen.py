import statistics
from statistics import mode

def most_common(namen):
    return(mode(namen))

namen = []
for A in range(100000):
    B = input('naam: ')
    namen.append(B)
    if B == "uitslag":
        print(most_common(namen))
