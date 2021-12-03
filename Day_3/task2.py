import math

oxygen_rating = 0
co2_rating = 0
length = 0

n_bits = 12

common = [0] * n_bits
anti = [0] * n_bits
numbers = []


def new_bitmap(old_list):
    new_list = [0] * n_bits
    for num in old_list:
        for j, bit in enumerate(num):
            new_list[j] += bit
    return new_list

with open("data.txt", "r") as f: 
    lines = f.readlines()
    length = len(lines)
    for line in lines: 
        bitmap = list(line.strip("\n"))
        bitmap = [int(bit) for bit in bitmap]
        numbers.append(bitmap)
        #print(bitmap)
        for j, bit in enumerate(bitmap):
            common[j] += bit

# Let's find oxygen generator rating first 

numbers_copy = [number for number in numbers]

for i in range(n_bits):
    # Update common
    common = new_bitmap(numbers)
    # if more 1s in bit i
    if common[i] >= len(numbers)/2:
        most_c = 1
    else: 
        most_c = 0 
    
    #print(f"In round {i+1}, most common: {most_c}")
    numbers[:] = [number for number in numbers if (number[i] == most_c)]
    
    #print(numbers)
    if len(numbers) < 2: 
        break

oxygen_rating = int("".join(str(bit) for bit in numbers[0]), 2)
print("O2:",oxygen_rating)

for i in range(n_bits):
    # Update common
    common = new_bitmap(numbers_copy)
    # if more 1s in bit i
    if common[i] >= len(numbers_copy)/2:
        most_c = 1
    else: 
        most_c = 0 
    
    #print(f"In round {i+1}, most common: {most_c}")
    numbers_copy[:] = [number for number in numbers_copy if (number[i] != most_c)]
    
    #print(numbers_copy)
    if len(numbers_copy) < 2: 
        break

co2_rating = int("".join(str(bit) for bit in numbers_copy[0]), 2)
print("CO2:", co2_rating)

print("Answer: ", oxygen_rating*co2_rating)


        