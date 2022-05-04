def countdown(number):
    if number == 0:
        print("Done")
        return
    else:
        print(number)
        countdown(number - 1)


countdown(5)
