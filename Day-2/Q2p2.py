hor = 0
dep = 0
aim = 0

with open("input.txt") as f:
  for l in f:
    s_arr = l.split(" ")
    if s_arr[0] == "forward":
      hor += int(s_arr[1])
      dep += aim * int(s_arr[1])
    elif s_arr[0] == "up":
      aim -= int(s_arr[1])
    elif s_arr[0] == "down":
      aim += int(s_arr[1])
    else:
      raise Exception("invalid input")

print(hor)
print(dep)
print(hor*dep)