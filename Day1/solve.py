import os, sys

def solution1(data):
    count = 0
    first = data[0]
    for l in data:
        l = int(l)
        if l > first:
            count += 1
        first = l
    return count

def solution2(data):
    output = []
    for i in range(0, len(data) - 2):
        output.append(data[i] + data[i + 1] + data[i+2])
    return output

data = [int(line.strip()) for line in open(os.path.join(sys.path[0], "input.txt"), 'r')]

print(solution1(data))
print(solution1(solution2(data)))