def bubble(values):
    for i in range(0, len(values) - 1, 1):
        for j in range(0, len(values) - i - 1, 1):
            if values[j] > values[j + 1]:
                temp = values[j]
                values[j] = values[j + 1]
                values[j + 1] = temp
    print(values)


bubble([5, 4, 7, 9, 2, 5, 6, 1])
