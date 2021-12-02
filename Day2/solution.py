import os, sys
data = [line.strip() for line in open(os.path.join(sys.path[0], "input.txt"), 'r')]

def horizontalDepthMultiply(inputdata):
    horizontal = 0
    depth = 0
    for row in inputdata:
        movement = int(row.split(' ')[1])
        if 'up' in row:
            depth -= movement
        if 'down' in row:
            depth += movement
        if 'forward' in row:
            horizontal += movement
    
    return horizontal * depth

print(horizontalDepthMultiply(data))

def horizontalDepthAimMultiply(inputdata):
    horizontal = 0
    depth = 0
    aim = 0
    for row in inputdata:
        movement = int(row.split(' ')[1])
        if 'up' in row:
            aim -= movement
        if 'down' in row:
            aim += movement
        if 'forward' in row:
            horizontal += movement
            depth += (movement * aim)

    return horizontal * depth

print(horizontalDepthAimMultiply(data))