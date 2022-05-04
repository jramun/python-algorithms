def selection(values):
    for i in range(0, len(values) - 1, 1):
        index = i
        for j in range(i + 1, len(values), 1):
            if values[j] < values[index]:
                index = j
        temp = values[index]
        values[index] = values[i]
        values[i] = temp
    print(values)


selection([5, 4, 7, 9, 2, 5, 6, 1])
