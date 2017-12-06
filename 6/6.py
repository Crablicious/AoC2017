with open("input.txt", "r") as f:
    data = f.read().split()

data = [int(x) for x in data]
print(data)

known_sets = [data[:]]

counter = 0
while True:
    counter += 1
    largest = 0
    ptr = 0
    for d in data:
        if d > largest:
            largest = d

    i = data.index(largest)
    data[i] = 0
    ptr = (i + 1) % len(data)

    for _ in range(largest):
        data[ptr] += 1
        ptr = (ptr + 1) % len(data)
        largest -= 1

    if data in known_sets:
        break
    else:
        known_sets.append(data[:])

print(counter)
