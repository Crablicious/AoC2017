with open("input.txt", "r") as f:
    data = f.read()[:-1]

level = 0
score = 0
is_garbage = False
skip_next = False
garbage_count = 0

for i in range(len(data)):
    c = data[i]
    if not is_garbage:
        if c == '{':
            level += 1
            score += level
        elif c == '}':
            level -= 1
        elif c == ',':
            pass
        elif c == '<':
            is_garbage = True
    else:
        if skip_next:
            skip_next = False
            continue
        elif c == '>':
            is_garbage = False
        elif c == '!':
            skip_next = True
        else:
            garbage_count += 1

print('Total score: ' + str(score))
print('Garbage count: ' + str(garbage_count))
