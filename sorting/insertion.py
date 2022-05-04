def insertion(values):
    for i in range(1, len(values), 1):
        value = values[i]
        j = i - 1
        while j >= 0 and values[j] > value:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = value
    print(values)


values = [5, 4, 7, 9, 2, 5, 6, 1]
insertion(values)
