with open("input.txt", "r") as f:
    data = f.read().split('\n')[:-1]

data = [int(x) for x in data]

ptr = 0
steps = 0
try:
    while True:
        tmp = ptr
        ptr += data[ptr]
        if data[tmp] > 2:
            data[tmp] -= 1
        else:
            data[tmp] += 1
        steps += 1
except IndexError:
    print(data)
    print(steps)
