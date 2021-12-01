"""
Day 1, task 2 of Advent of Code 2021. 
"""
count = 0

with open("data.txt", "r") as f:
    lines = f.readlines()

    i = 0
    current = 0
    lines = [int(x) for x in lines]

    for line in lines:
        if(len(lines) - i >= 4):
            sum1 = lines[i] + lines[i+1] + lines[i+2]
            sum2 = lines[i+1] + lines[i+2] + lines[i+3]
            if(sum2 > sum1):
                count = count + 1
            i += 1

print(count)
