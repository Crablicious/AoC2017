import binascii


def knot_hash(data):
    lengths = [ord(x) for x in data]
    length_suffix = [17, 31, 73, 47, 23]
    lengths.extend(length_suffix)

    nums = []
    for i in range(256):
        nums.append(i)

    curr_pos = 0
    skip_size = 0
    for _ in range(64):
        for l in lengths:
            rev_l = []
            for i in range(l):
                rev_l.append(nums[(curr_pos + i) % len(nums)])
            rev_l.reverse()
            for i in range(l):
                nums[(curr_pos + i) % len(nums)] = rev_l[i]

            curr_pos = curr_pos + skip_size + l
            skip_size += 1

    sparse_hash = nums
    dense_hash = []
    for i in range(16):
        val = sparse_hash[i*16]
        for j in range(15):
            val = val ^ sparse_hash[i*16+j+1]
        dense_hash.append(val)

    khash = ''
    for n in dense_hash:
        khash += '{:02X}'.format(n)

    return khash


def kill_neighbors(x, y):
    if grid[(x, y)] == '0':
        return
    else:
        grid[(x, y)] = '0'
        try:
            kill_neighbors(x+1, y)
        except:
            pass
        try:
            kill_neighbors(x-1, y)
        except:
            pass
        try:
            kill_neighbors(x, y+1)
        except:
            pass
        try:
            kill_neighbors(x, y-1)
        except:
            pass


inp = 'vbqugkhl-'
total_ones = 0
grid = {}

for row in range(128):
    key = inp+str(row)
    hexahash = knot_hash(key)
    # magic line from stackoverflow
    string = ''.join([bin(int(x, 16)+16)[3:] for y, x in enumerate(hexahash)])
    total_ones += string.count('1')
    for i in range(len(string)):
        grid[(i, row)] = string[i]

print(total_ones)

regions = 0
for y in range(128):
    for x in range(128):
        if grid[(x, y)] == '1':
            regions += 1
            kill_neighbors(x, y)

print(regions)
