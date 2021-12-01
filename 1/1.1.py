#opens the data file, seperated each value by line, converts the value to an int, and saves into "data" list.
with open("data.txt") as tmpfile:
    data =[int(line.rstrip("\n")) for line in tmpfile]

#loops through the list and increases count if current > last. Starts the loop on 2nd val in list with last set as the
#first value already.
last = data[0]
total = 0
for x in range(1, len(data)):
    if data[x] > last:
        total += 1
    last = data[x]
print(total)