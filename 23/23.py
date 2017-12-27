from collections import defaultdict


def is_prime(a):
    if a < 2:
        return False
    return all(a % i for i in range(2, a))


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

regs = defaultdict(int)
regs['a'] = 1
mul_count = 0
i = 0

while i >= 0 and i < len(data):
    if i == 11:
        regs['g'] = 0
        regs['e'] = regs['b']
        regs['d'] = regs['b']
        i = 24

        if not is_prime(regs['b']):
            regs['f'] = 0

        continue

    line = data[i].split()

    if line[0] == 'set':
        try:
            val = int(line[2])
        except:
            val = regs[line[2]]

        regs[line[1]] = val
    elif line[0] == 'sub':
        try:
            val = int(line[2])
        except:
            val = regs[line[2]]
        regs[line[1]] -= val
    elif line[0] == 'mul':
        mul_count += 1
        try:
            val = int(line[2])
        except:
            val = regs[line[2]]
        regs[line[1]] *= val
    elif line[0] == 'jnz':
        try:
            val0 = int(line[1])
        except:
            val0 = regs[line[1]]

        try:
            val1 = int(line[2])
        except:
            val1 = regs[line[2]]
        if val0 != 0:
            i += val1
            continue
    i += 1

print(mul_count)
print('reg h:' + str(regs['h']))
