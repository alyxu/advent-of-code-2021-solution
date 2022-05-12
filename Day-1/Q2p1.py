hor = 0
dep = 0

with open("sample.txt") as f:
  for l in f:
    s_arr = l.split(" ")
    if s_arr = "forward":
      hor += int(s_arr[1])
    elif s_arr = "up":
      dep -= int(s_arr[1])
    elif s_arr = "down":
      dep += int(s_arr[1])
    else:
      raise Exception("invalid input")

print(hor)
print(dep)
print(hor*dep)