def power(number, pwr):
    if pwr == 0:
        return 1
    else:
        return number * power(number, pwr - 1)


print(power(5, 3))
