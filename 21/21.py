import math


with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

rules_2 = []
rules_3 = []

for line in data:
    line = line.split(' => ')
    line[0] = line[0].split('/')
    line[1] = line[1].split('/')
    if len(line[0]) == 2:
        rules_2.append(line)
    else:
        rules_3.append(line)


def rotate_right(rule, n):
    for i in range(n):
        rule_tup = list(zip(*rule[::-1]))
        rule = []
        for i in range(len(rule_tup)):
            rule.append(''.join(rule_tup[i]))
    return rule

rules_2_perm = []
for rule in rules_2:
    output = rule[1]
    flipped_rule = [x[::-1] for x in rule[0]]
    for i in range(4):
        rotated = rotate_right(rule[0], i)
        flipped_rotated = rotate_right(flipped_rule, i)
        rules_2_perm.append([rotated, output])
        rules_2_perm.append([flipped_rotated, output])

rules_3_perm = []
for rule in rules_3:
    output = rule[1]
    flipped_rule = [x[::-1] for x in rule[0]]
    for i in range(4):
        rotated = rotate_right(rule[0], i)
        flipped_rotated = rotate_right(flipped_rule, i)
        rules_3_perm.append([rotated, output])
        rules_3_perm.append([flipped_rotated, output])


art = ['.#.', '..#', '###']

for _ in range(18):
    if len(art) % 2 == 0:
        divisor = 2
        rules = rules_2_perm
    else:
        divisor = 3
        rules = rules_3_perm

    arts = []
    for k in range(len(art)):
        arts.append([
            art[k][i:i + divisor] for i in range(0, len(art[k]), divisor)])

    arts2 = []
    for k in range(len(arts) // divisor):
        for i in range(len(arts[0])):
            tmp = []
            for j in range(divisor):
                tmp.append(arts[(k*divisor)+j][i])
            arts2.append(tmp)

    art = []
    for part in arts2:
        for rule in rules:
            match = True
            for i in range(divisor):
                if rule[0][i] != part[i]:
                    match = False
                    break
            if match:
                art.append(rule[1])
                break

    tmp_art = []
    append_i = 0
    line_length = int(math.sqrt(len(art)))

    for i in range(line_length):
        tmp_art.append(art[i*line_length][:])
        leng = len(tmp_art[i][0])
        for j in range(1, line_length):
            for k in range(leng):
                tmp = art[i*line_length+j][k]
                tmp_art[i][k] += tmp

    final_art = []
    for i in range(line_length):
        for j in range(len(tmp_art[0])):
            final_art.append(tmp_art[i][j])

    if line_length == 0:
        for j in range(len(art[0])):
            final_art.append(art[0][j])

    art = final_art

count = 0
for row in art:
    count += row.count('#')

print(count)
