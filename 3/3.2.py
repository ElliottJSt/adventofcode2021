with open("data.txt") as tmpfile:
    data = [line.rstrip("\n") for line in tmpfile]


def recursiveNewList(input, Depth, O2srch):
    newList= []
    valBalance = 0
    for each in input:
        if each[Depth] == "1":
            valBalance += 1
        elif each[Depth] == "0":
            valBalance -= 1

    if O2srch:
        if valBalance >= 0:
            newListIndexes = [y for y in range(len(input)) if (input[y])[Depth] == "1"]
        elif valBalance < 0:
            newListIndexes = [y for y in range(len(input)) if (input[y])[Depth] == "0"]
    else:
        if valBalance >= 0:
            newListIndexes = [y for y in range(len(input)) if (input[y])[Depth] == "0"]
        elif valBalance < 0:
            newListIndexes = [y for y in range(len(input)) if (input[y])[Depth] == "1"]

    for each in newListIndexes:
        newList.append(input[each])

    if len(newList) != 1:
        Depth += 1
        return recursiveNewList(newList, Depth, O2srch)
    else:
        return newList


O2 = int((recursiveNewList(data, 0, True))[0], 2)
CO2 = int((recursiveNewList(data, 0, False))[0], 2)
print("Life support rating =", O2 * CO2)