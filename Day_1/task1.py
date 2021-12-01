"""
Day 1, task 1 of Advent of Code 2021
"""

count = -1

with open("data.txt", "r") as f:
    lines = f.readlines()

    i = 0
    current = 0
    for line in lines:
        line = int(line)
        if line > current: 
            count = count + 1
        current = line

print(count)