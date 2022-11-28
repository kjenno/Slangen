def bubbleSort(arr):
    A = len(arr)

    swapped = False

    for B in range(A):

        for C in range(0, A-B-1):

            if arr[C] > arr[C + 1]:
                swapped = True
                arr[C], arr[C + 1] = arr[C + 1], arr[C]

        if not swapped:
            return



arrr = [64, 34, 25, 12, 22, 11, 90, 77, 66, 54, 35, 11]

bubbleSort(arrr)

print("Gesorteerd V:")
for B in range(len(arrr)):
    print(arrr[B], end=" ")