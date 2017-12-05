with open("real_input.txt", "r") as f:
    data = f.read().strip('\n')

print(data)

# 1122
counter = 0
for i in range(len(data)):
    if data[i] == data[(i+1) % len(data)]:
        counter += int(data[i])

print(counter)
