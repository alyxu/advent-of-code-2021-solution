#Load list of numbers
#Loop through each bit in one number
#Iterate number of 0 bits and number of 1 bits for each pos
#We create a list containing num of 0 bits for each pos
#same with 1 bits
#Go through each number

with open("input.txt") as f:
    input_list = f.read().splitlines()

num_0 = [0 for i in range(len(input_list[0]))]
num_1 = [0 for i in range(len(input_list[0]))]

for num in input_list:
    for i, bit in enumerate(num):
        if bit == "0":
            num_0[i] += 1
        elif bit == "1":
            num_1[i] += 1
        else:
            raise Exception("invalid input")

print(num_0)
print(num_1)

gamma_bin = [0 if num_0[i] > num_1[i] else 1 
            for i in range(len(input_list[0]))]

epsilon_bin = [1 if num_0[i] > num_1[i] else 0
            for i in range(len(input_list[0]))]

print(int("".join(map(str,epsilon_bin)),2) * int("".join(map(str,gamma_bin)),2))
