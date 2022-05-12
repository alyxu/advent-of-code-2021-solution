#Faster solution
#Sort list based on position
#Count just one bit and immediately can obtain other bit by taking differene
#Then immediately discount the rest

with open("input.txt") as f:
    input_list = f.read().splitlines()

ox_gen_num = input_list.copy()
co2_scrub_rat = input_list.copy()

for pos in range(len(input_list[0])):
    num_0_ox = 0
    num_1_ox = 0
    for num in ox_gen_num:
        if num[pos] == "0":
            num_0_ox += 1
        elif num[pos] == "1":
            num_1_ox += 1
        else:
            raise Exception("invalid input")

    if len(ox_gen_num) > 1:
        if num_0_ox > num_1_ox:
            #0 is the most common value
            #1 is the least common vale
            ox_gen_num = list(filter(
                lambda x: True if x[pos] == "0" else False, ox_gen_num
                ))
        elif num_0_ox < num_1_ox:
            ox_gen_num = list(filter(
                lambda x: True if x[pos] == "1" else False, ox_gen_num
                ))
        else:
            #case where num_0_ox == num_1_ox
            ox_gen_num = list(filter(
                lambda x: True if x[pos] == "1" else False, ox_gen_num
                ))
    else:
        print("ox")
        print(int(ox_gen_num[0],2))

    num_0_co2 = 0
    num_1_co2 = 0
    for num in co2_scrub_rat:
        if num[pos] == "0":
            num_0_co2 += 1
        elif num[pos] == "1":
            num_1_co2 += 1
        else:
            raise Exception("invalid input")
    if len(co2_scrub_rat) > 1:
        if num_0_co2 > num_1_co2:
            #0 is the most common value
            #1 is the least common vale
            co2_scrub_rat = list(filter(
                lambda x: True if x[pos] == "1" else False, co2_scrub_rat
                ))
        elif num_0_co2 < num_1_co2:
            co2_scrub_rat = list(filter(
                lambda x: True if x[pos] == "0" else False, co2_scrub_rat
                ))
        else:
            #case where num_0 == num_1_co2
            co2_scrub_rat = list(filter(
                lambda x: True if x[pos] == "0" else False, co2_scrub_rat
                ))
    else:
        print("co2")
        print(int(co2_scrub_rat[0],2))

print("ox")
print(int(ox_gen_num[0],2))

print("co2")
print(int(co2_scrub_rat[0],2))

print(int(co2_scrub_rat[0],2) * int(ox_gen_num[0],2))