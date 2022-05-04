dictionary1 = dict({"key1": "value1", "key2": "value2", "key3": "value3", "key4": "value4"})
print(dictionary1)

dictionary2 = {}
dictionary2["key1"] = 1
dictionary2["key2"] = 2
dictionary2["key3"] = 3
dictionary2["key4"] = 4
print(dictionary2)

for key, value in dictionary2.items():
    print(key, " ", value)

if __name__ == '__main__':
    print("")
