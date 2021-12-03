# gamma rate is most common bit per group
# epsilon rate is least common bit per group
with open("data.txt") as tmpfile:
    data = [line.rstrip("\n") for line in tmpfile]

gammaRate = "0b"  # initialises rates as binary
epsilonRate = "0b"
temp1 = 0
temp0 = 0

for x in range(0, len(data[0])):
    for each in data:
        if each[x] == "1":
            temp1 += 1
        else:
            temp0 += 1
    if temp1 > temp0:  # 1 most common
        gammaRate += "1"
        epsilonRate +="0"
    elif temp0 > temp1:  # 0 most common
        gammaRate += "0"
        epsilonRate += "1"
    temp0 = temp1 = 0

print(int(gammaRate, 2), int(epsilonRate, 2))
print(int(gammaRate, 2) * int(epsilonRate, 2))