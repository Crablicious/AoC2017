with open("real_input.txt", "r") as f:
    data = f.readlines()

counter = 0
for line in data:
    line = [int(c) for c in line.strip('\n').split()]
    largest = line[0]
    smallest = line[0]
    for n in line:
        if n < smallest:
            smallest = n
        elif n > largest:
            largest = n
    counter += largest - smallest

    print(counter)

print(counter)
