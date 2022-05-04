def insertion(values):
    for i in range(1, len(values) - 1, 1):
        value = values[i]
        j = i - 1
        while j <= 0 & values[j] > value:
            values[j + 1] = values[j]
            j = j - 1
        values[j + 1] = value
    print(values)


insertion([5, 4, 7, 9, 2, 5, 6, 1])
