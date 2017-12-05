with open("real_input.txt", "r") as f:
    data = f.read().strip('\n')

counter = 0
halfway = len(data)//2
for i in range(len(data)):
    if data[i] == data[(i+halfway) % len(data)]:
        counter += int(data[i])

print(counter)
