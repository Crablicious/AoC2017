def is_hit_stupid(depth, timesteps):
    direc = 1
    pos = 0
    while(timesteps > 0):
        pos += direc
        if pos == 0 or pos == depth-1:
            direc = -direc

        timesteps -= 1
    return pos == 0


def is_hit(depth, timesteps):
    offset = timesteps % (depth-1)
    up_or_down = timesteps // (depth-1)
    if up_or_down % 2 == 0:
        pos = offset
    else:
        pos = depth-offset

    return pos == 0


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

i = 0
while (True):
    severity = 0

    for line in data:
        line = line.split()
        layer = int(line[0].strip(':'))
        depth = int(line[1])

        timesteps = i + layer
        if is_hit(depth, timesteps):
            severity = 1
            break
            # severity += layer*depth

    if severity == 0:
        print('severity 0')
        print(i)
        break

    i += 1
