num_incread = 0
prev = None

with open("input.txt") as f:
  input_list = f.read().splitlines() 

prev = None
for i,val in enumerate(input_list):
  #Deal with looping back every 5th 
  #Deal with OOB
  if i+3 <= len(input_list):
    current = int(input_list[i]) + int(input_list[i+1]) + int(input_list[i+2])
    if prev is not None:
      if current > prev:
        num_incread += 1
    prev = current

print(num_incread)