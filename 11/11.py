from operator import add

# blatant theft of coordinate transformations from
# https://www.redblobgames.com/grids/hexagons/#conversions


def cube_distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


def axial_to_cube(pos):
    x = pos[0]
    z = pos[1]
    y = -x-z
    return [x, y, z]


def distance(a, b):
    ac = axial_to_cube(a)
    bc = axial_to_cube(b)
    return cube_distance(ac, bc)


with open("input.txt", "r") as f:
    data = f.read()[:-1].split(',')

pos = [0, 0]

d = {'n': [0, -1], 'ne': [1, -1], 'se': [1, 0],
     's': [0, 1], 'sw': [-1, 1], 'nw': [-1, 0]}

highest = 0
for direc in data:
    pos = list(map(add, d[direc], pos))
    highest = max(highest, distance(pos, [0, 0]))

print(pos)

print(distance(pos, [0, 0]))
print(highest)
