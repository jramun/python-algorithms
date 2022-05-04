def mergeSort(values):
    if len(values) > 1:
        mid = len(values) // 2
        arrayLeft = values[0:mid]
        arrayRight = values[mid:len(values)]
        print('Left     ', arrayLeft, '     Right   ', arrayRight)
        mergeSort(arrayLeft)
        mergeSort(arrayRight)
        merge(values, arrayLeft, arrayRight)
        print('Values   ', values)


def merge(values, array1, array2):
    counter1 = 0
    counter2 = 0
    counter = 0

    while counter1 < len(array1) and counter2 < len(array2):
        if array1[counter1] < array2[counter2]:
            values[counter] = array1[counter1]
            counter1 += 1
        else:
            values[counter] = array2[counter2]
            counter2 += 1
        counter += 1

    while counter1 < len(array1):
        values[counter] = array1[counter1]
        counter += 1
        counter1 += 1

    while counter2 < len(array2):
        values[counter] = array2[counter2]
        counter += 1
        counter2 += 1


datasets = [5, 4, 7, 9, 2, 5, 6, 1]
print(datasets)
mergeSort(datasets)
print(datasets)
