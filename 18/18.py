from collections import defaultdict


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

registers = defaultdict(int)

i = 0
while i >= 0 and i < len(data):
    instr = data[i].split()
    if len(instr) > 2:
        try:
            val = int(instr[2])
        except:
            val = registers[instr[2]]

    if instr[0] == 'set':
        registers[instr[1]] = val
    elif instr[0] == 'snd':
        last_freq = registers[instr[1]]
    elif instr[0] == 'add':
        registers[instr[1]] += val
    elif instr[0] == 'mul':
        registers[instr[1]] *= val
    elif instr[0] == 'mod':

        registers[instr[1]] = registers[instr[1]] % val
    elif instr[0] == 'rcv':
        if registers[instr[1]] > 0:
            recovered = last_freq
            break
    elif instr[0] == 'jgz':
        if registers[instr[1]] > 0:
            i += val
            continue

    i += 1

print(recovered)
