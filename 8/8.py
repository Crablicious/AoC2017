from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.readlines()

highest = 0

d = defaultdict(int)
for l in lines:
    l = l.split()
    reg = l[0]
    op = l[1]
    val = int(l[2])
    if op == 'dec':
        val = -val

    cmpreg = l[4]
    cmpval0 = d[cmpreg]
    cmpop = l[5]
    cmpval1 = l[6]

    b = eval(str(cmpval0) + cmpop + cmpval1)
    if b:
        d[reg] += val

    high = max(d.values())
    if high > highest:
        highest = high

print(max(d.values()))
print(highest)
