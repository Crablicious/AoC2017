with open("input.txt", "r") as f:
    data = f.readlines()

counter = 0

for line in data:
    words = line.strip('\n').split()
    duplicates = False

    sorted_words = [''.join(sorted(w)) for w in words]

    for word in sorted_words:
        if sorted_words.count(word) > 1:
            duplicates = True
            break

    if not duplicates:
        counter += 1

print(counter)
