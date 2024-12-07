fopen = open("data.txt", "r")

order = dict()
updates = []

def fix_update(order, update) -> list[int]:
    valid = True
    restricted = []
    for i in range(len(update)):
        for record in restricted:
            if update[i] in record[1]:
                valid = False
                update[i], update[record[0]] = update[record[0]], update[i]
                break
        if update[i] in order:
            restricted.append((i, order[update[i]]))
    if not valid:
        update = fix_update(order, update)
    return update

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
    restricted = []
    for i in range(len(update)):
        for record in restricted:
            if update[i] in record[1]:
                valid = False
                break
        if update[i] in order:
            restricted.append((i, order[update[i]]))
    if not valid:
        update = fix_update(order, update)
        total += update[len(update)//2]

print(total)
