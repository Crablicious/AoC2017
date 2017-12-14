import time


def create_grid(last_value):
    last_run = 0

    grid = {}
    grid[(0, 0)] = 1
    grid[(1, 0)] = 1
    direc = (0, 0)
    pos = [1, 0]
    layer = 1
    while True:
        for i in range(4):
            steps = layer * 2
            print(pos)
            if i == 0:
                direc = (0, -1)
                steps -= 1
            elif i == 1:
                direc = (-1, 0)
            elif i == 2:
                direc = (0, 1)
            elif i == 3:
                direc = (1, 0)
                steps += 1
            for j in range(steps):
                pos[0] += direc[0]
                pos[1] += direc[1]
                val = 0
                try:
                    neighbor = (pos[0]-1, pos[1])
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0]+1, pos[1])
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0], pos[1]-1)
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0], pos[1]+1)
                    val += grid[neighbor]
                except KeyError:
                    pass

                try:
                    neighbor = (pos[0]+1, pos[1]+1)
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0]-1, pos[1]+1)
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0]+1, pos[1]-1)
                    val += grid[neighbor]
                except KeyError:
                    pass
                try:
                    neighbor = (pos[0]-1, pos[1]-1)
                    val += grid[neighbor]
                except KeyError:
                    pass

                grid[(pos[0], pos[1])] = val

                if val > last_value:
                    return val

        layer += 1
        print(grid)

print(create_grid(265149))
