
x = 0
depth = 0

with open("data.txt", "r+") as f: 
    lines = f.readlines()

    for line in lines: 
        commands = line.split(" ")
        direction = commands[0]
        val = int(commands[1])
        match direction:
            case "down":
                depth += val
            case "up":
                depth -= val
            case "forward":
                x += val
            case _:
                continue

print(x*depth)