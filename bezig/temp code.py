# def bubbleSort(arr):
#     n = len(arr)

#     swapped = False

#     for i in range(n):

#         for j in range(0, n-i-1):

#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#         if not swapped:
#             return



# arr = [64, 34, 25, 12, 22, 11, 90, 77, 66, 54, 35, 11]

# bubbleSort(arr)

# print("Gesorteerd V:")
# for i in range(len(arr)):
#     print(arr[i], end=" ")

import datetime

x = datetime.datetime.now()
print(x)
