def next_val(gen_vals, factors, divider):
    multiple = 4
    for i in range(len(gen_vals)):
        found = False
        while not found:
            gen_vals[i] = (gen_vals[i]*factors[i]) % divider
            if gen_vals[i] % (multiple*(i+1)) == 0:
                found = True

gen_vals = [634, 301]
factors = [16807, 48271]
divider = 2147483647

count = 0

for i in range(5000000):
    if i % 1000000 == 0:
        print(i)

    next_val(gen_vals, factors, divider)
    bin_strs = []
    for i in range(len(gen_vals)):
        bin_str = '{0:b}'.format(gen_vals[i])
        bin_strs.append(bin_str[len(bin_str)-16:])

    if set(bin_strs) != len(bin_strs):
        count += 1

print(count)
