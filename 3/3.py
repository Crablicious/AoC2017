def create_grid(last_value):
    pos = [0, 0]
    value = 1
    layer = 0
    layer_max = 1
    while value != last_value:
        if value == layer_max:
            pos[0] += 1


def calculate_layer(last_value):
    pos = [0, 0]
    value = 1
    layer = 0
    layer_max = 1
    while layer_max < last_value:
        layer += 1
        layer_max = layer_max + 8 * layer

    return layer, layer_max

val = 265149
layer, layer_max = calculate_layer(val)
print(layer, layer_max)

diff = layer_max - val

pos = [layer, layer]

w = 1 + layer * 2 - 1

steps = layer_max - val

for i in range(w):
    if steps > 0:
        pos[0] -= 1
        steps -= 1

for i in range(w):
    if steps > 0:
        pos[1] -= 1
        steps -= 1

for i in range(w):
    if steps > 0:
        pos[0] += 1
        steps -= 1

for i in range(w):
    if steps > 0:
        pos[1] += 1
        steps -= 1

print(pos)
print(abs(pos[0]) + abs(pos[1]))
