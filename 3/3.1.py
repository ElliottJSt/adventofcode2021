# gamma rate is most common bit per group
# epsilon rate is least common bit per group
with open("data.txt") as tmpfile:
    data = [line.rstrip("\n") for line in tmpfile]

epsilonRate, gammaRate, valBalance = "", "", 0
print(epsilonRate, gammaRate, valBalance)
for x in range(0, len(data[0])):
    for each in data:
        if each[x] == "1":
            valBalance += 1
        elif each[x] == "0":
            valBalance -= 1

    if valBalance > 0:  # 1 most common
        gammaRate += "1"
        epsilonRate += "0"
    elif valBalance < 0:  # 0 most common
        gammaRate += "0"
        epsilonRate += "1"
    valBalance = 0
print("Power Consumption = ", int(gammaRate, 2) * int(epsilonRate, 2))