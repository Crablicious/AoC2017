inp = 371

# first part
circ_buf = [0]
curr_pos = 0

for i in range(1, 2018):
    next_pos = (curr_pos + inp) % len(circ_buf)
    curr_pos = next_pos+1
    circ_buf.insert(curr_pos, i)

print(circ_buf[(circ_buf.index(2017)+1) % len(circ_buf)])

# second part
curr_pos = 0
length = 1
last_index_one = 0

for i in range(1, 50000001):
    next_pos = (curr_pos + inp) % length
    length += 1
    curr_pos = next_pos+1
    if curr_pos == 1:
        last_index_one = i

print(last_index_one)
