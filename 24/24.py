import sys


def get_ports(ports, n):
    result = []
    for port in ports:
        if n in port:
            result.append(port)
    return result


def probe(ports, port, open_port):
    ports.remove(port)
    matches = get_ports(ports, open_port)
    vals = []
    depths = []
    for match in matches:
        if match[0] == open_port:
            depth, val = probe(ports[:], match, match[1])
            depths.append(depth)
            vals.append(val)
        else:
            depth, val = probe(ports[:], match, match[0])
            depths.append(depth)
            vals.append(val)

    if vals:
        deepest = [i for i, x in enumerate(depths) if x == max(depths)]
        deepest_vals = []
        for i in deepest:
            deepest_vals.append(vals[i])
        large_i = deepest_vals.index(max(deepest_vals))
        return 1+depths[deepest[large_i]], sum(port) + deepest_vals[large_i]
    else:
        return 1, sum(port)


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')


ports = []

for line in data:
    line = line.split('/')
    ports.append([int(line[0]), int(line[1])])

print(ports)

starts = []
for port in ports:
    if 0 in port:
        starts.append(port)

print(starts)

strongest = 0
open_port = 0
points = []

for start in starts:
    matches = get_ports(ports, open_port)
    vals = []

    for match in matches:
        if match[0] == open_port:
            vals.append(probe(ports[:], match, match[1]))
        else:
            vals.append(probe(ports[:], match, match[0]))

print(vals)
print(points)
