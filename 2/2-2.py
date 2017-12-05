def line_loop(line):
    for n1 in line:
        for n2 in line:
            if n1 != n2 and n1 % n2 == 0:
                return n1 // n2

with open("real_input.txt", "r") as f:
    data = f.readlines()

counter = 0
for line in data:
    line = [int(c) for c in line.strip('\n').split()]
    counter += line_loop(line)

print(counter)
