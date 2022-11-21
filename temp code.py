def bubble (list_a):
    indexing_length = len(list_a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range (0, indexing_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[1], list_a[i+1] = list_a[i+1], list_a[1]
    return list_a

print(bubble([4,6,2,3,7,9]))