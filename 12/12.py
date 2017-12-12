with open("input.txt", "r") as f:
    data = f.read().split('\n')[:-1]

groups = []

for l in data:
    l = l.split()

    conns = [int(l[0])]
    for i in range(len(l)-2):
        conns.append(int(l[i+2].strip(',')))

    conn_groups = []
    for g in groups:
        for conn in conns:
            if conn in g:
                conn_groups.append(g)
                conns += g
                break

    for g in conn_groups:
        groups.remove(g)

    groups.append(conns)

for g in groups:
    if 0 in g:
        print(len(set(g)))

print(len(groups))
