fopen = open("data.txt", "r")

order = dict()
updates = []

read_mode = 0
for line in fopen:
    if line == "\n":
        read_mode = 1
        continue

    if read_mode == 0:
        parts = line.split("|")
        key = int(parts[1])
        value = int(parts[0])
        if key not in order:
            order[key] = set()
        order[key].add(value)

    if read_mode == 1:
        parts = line.split(",")
        updates.append([int(part) for part in parts])

total = 0
for update in updates:
    valid = True
    restricted = set()
    for num in update:
        if num in restricted:
            valid = False
            break
        restricted.update(order.get(num, set()))
    if valid:
        total += update[len(update)//2]

print(total)
