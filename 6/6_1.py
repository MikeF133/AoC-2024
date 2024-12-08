DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def main():
    fopen = open("data.txt", "r")
    obstacles = set()
    visited = set()
    direction = 0
    pos = (0, 0)

    i = -1
    for line in fopen:
        i += 1
        line = line.strip()
        j = -1
        for c in line:
            j += 1
            if c == "#":
                obstacles.add((i, j))
                continue
            if c == "^":
                pos = (i, j)
                visited.add(pos)
    
    max_pos = i
    
    while True:
        if (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1]) in obstacles:
            direction = turn_right(direction)
        pos = (pos[0] + DIRECTIONS[direction][0], pos[1] + DIRECTIONS[direction][1])
        if pos[0] < 0 or pos[0] > max_pos or pos[1] < 0 or pos[1] > max_pos:
            break
        visited.add(pos)

    print(len(visited))


def turn_right(x: int) -> int:
    return (x + 1) % 4

main()