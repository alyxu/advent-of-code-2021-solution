num_incread = 0
prev = None

with open("input.txt") as f:
  for line in f:
    current = int(line)
    if prev is None:
      next
    else:
      if current > prev:
        num_incread += 1
    prev = current

print(num_incread)
