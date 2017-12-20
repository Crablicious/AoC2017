with open("input.txt", "r") as f:
    data = f.read()[:-1].split('\n')

print(data)

map_chars = ['+', '-', '|', ' ']

# find start
start = data[0].index('|')

# y x
pos = [0, start]
print(pos)
direc = [1, 0]

letters = []

last_char = ' '

steps = 0

while (data[pos[0]][pos[1]] != ' '):
    steps += 1
    pos[0] += direc[0]
    pos[1] += direc[1]
    x = pos[1]
    y = pos[0]
    print(pos)
    curr_char = data[y][x]
    if curr_char == '+':
        try:
            if data[y+1][x] != last_char and data[y+1][x] != ' ':
                direc = [1, 0]
        except:
            pass
        try:
            if data[y-1][x] != last_char and data[y-1][x] != ' ':
                direc = [-1, 0]
        except:
            pass

        try:
            if data[y][x+1] != last_char and data[y][x+1] != ' ':
                direc = [0, 1]
        except:
            pass

        try:
            if data[y][x-1] != last_char and data[y][x-1] != ' ':
                direc = [0, -1]
        except:
            pass

    elif curr_char not in map_chars:
        letters.append(curr_char)

    last_char = curr_char

print(letters)
print(''.join(letters))
print(steps)
