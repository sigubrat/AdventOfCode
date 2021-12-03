import math

gamma = 0
epsilon = 0
length = 0

n_bits = 12

common = [0] * n_bits
anti = [0] * n_bits

with open("data.txt", "r") as f: 
    lines = f.readlines()
    length = len(lines)
    for line in lines: 
        bitmap = list(line.strip("\n"))
        bitmap = [int(bit) for bit in bitmap]
        #print(bitmap)
        for j, bit in enumerate(bitmap):
            common[j] += bit

for i, bit in enumerate(common):
    if bit > math.ceil(length/2):
        common[i] = 1
        anti[i] = 0
    else: 
        common[i] = 0
        anti[i] = 1

gamma = int("".join(str(bit) for bit in common), 2)
epsilon = int("".join(str(bit) for bit in anti), 2)

print("Power consumption: ", gamma*epsilon)
        