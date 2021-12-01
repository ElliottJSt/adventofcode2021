#opens the data file, seperated each value by line, converts the value to an int, and saves into "data" list.
with open("data.txt") as tmpfile:
    data =[int(line.rstrip("\n")) for line in tmpfile]

#loops through the list and increases count if current > last. Starts the loop on 2nd val in list with last set as the
#first value already.
total = 0
#consists of first 3 values in the list (1,2,3) as the loop starts with values (2,3,4)
lastsum = data[0]+data[1]+data[2]
for x in range(1, len(data)-2):
    sum = data[x]+data[x+1]+data[x+2]
    if sum > lastsum:
        total += 1
    lastsum = sum
print(total)