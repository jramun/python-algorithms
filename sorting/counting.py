def counting(values):
    print(values)
    maximum = max(values)
    result = [0] * len(values)
    temp = [0] * (maximum + 1)
    for j in range(0, len(values), 1):
        temp[values[j]] = temp[values[j]] + 1
    print(temp)
    for k in range(1, len(temp), 1):
        temp[k] = temp[k] + temp[k - 1]
    print(temp)
    for item in values:
        result[temp[item] - 1] = item
        temp[item] -= 1
    print(result)


def max(values):
    max = values[0]
    for i in range(0, len(values) - 1, 1):
        if max < values[i]:
            max = values[i]
    return max


counting([5, 4, 7, 9, 2, 5, 6, 1])
