from collections import defaultdict


def turn_right(direc, n):
    for _ in range(n):
        if direc == [1, 0]:
            direc = [0, 1]
        elif direc == [-1, 0]:
            direc = [0, -1]
        elif direc == [0, 1]:
            direc = [-1, 0]
        elif direc == [0, -1]:
            direc = [1, 0]
    return direc

with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

grid = defaultdict(lambda: '.')
for i in range(len(data)):
    for j in range(len(data[i])):
        grid[(j, i)] = data[i][j]


curr = ((len(data[0])-1)//2, (len(data)-1)//2)
direc = [0, -1]

burst_infect_count = 0

for _ in range(10000):
    print(curr)
    print(direc)
    if grid[curr] == '#':
        direc = turn_right(direc, 1)
        grid[curr] = '.'
    else:  # clean
        direc = turn_right(direc, 3)
        grid[curr] = '#'
        print('infect')
        burst_infect_count += 1
    curr = (curr[0]+direc[0], curr[1]+direc[1])

print(burst_infect_count)
