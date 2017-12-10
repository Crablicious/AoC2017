with open("input.txt", "r") as f:
    data = f.read()[:-1]

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

print(khash)
