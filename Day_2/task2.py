
x = 0
depth = 0
aim = 0

with open("data.txt", "r+") as f: 
    lines = f.readlines()

    for line in lines: 
        commands = line.split(" ")
        direction = commands[0]
        val = int(commands[1])
        match direction:
            case "down":
                aim += val
            case "up":
                aim -= val
            case "forward":
                x += val
                depth += val * aim
            case _:
                continue

print(x*depth)