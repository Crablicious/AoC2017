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
    vals = [0]
    for match in matches:
        if match[0] == open_port:
            probe(ports[:], match, match[1])
            vals.append(probe(ports[:], match, match[1]))
        else:
            vals.append(probe(ports[:], match, match[0]))
    return 1+depth, sum(port) + max(vals)


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
