#opens the data file, seperated each value by line, converts the value to an int, and saves into "data" list.
with open("data.txt") as tmpfile:
  data = [line.rstrip("\n") for line in tmpfile]

forward = 0
depth = 0
for each in data:
  x = each.split(" ")
  if x[0] == "forward":
    forward += int(x[1])
  elif x[0] == "down":
    depth += int(x[1])
  elif x[0] == "up":
    depth -= int(x[1])
print(forward, "*", depth,"=",forward*depth)
