def counting(values):
    maximum = max(values)
    result = [len(values)]
    temp = [maximum + 1]
    for e in temp:
        e = 0
    for e in values:
        temp[e] += 1
    for k in range(1, len(temp) - 1, 1):
        temp[k] = temp[k] + temp[k - 1]
    for item in values:
        result[temp[item]] = item
        temp[item] -= 1
    print(result)


def max(values):
    max = values[0]
    for i in range(0, len(values) - 1, 1):
        if max < values[i]:
            max = values[i]
    return max


counting([5, 4, 7, 9, 2, 5, 6, 1])
