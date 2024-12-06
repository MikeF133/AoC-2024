FNAME = "data.txt"
WORD = "MMASS"


def main():
    matrix = file_to_matrix(FNAME)
    print(count_word(matrix, WORD))

def file_to_matrix(fname: str) -> list[list]:
    out = []
    fopen = open(fname, "r")
    for line in fopen:
        out.append([c for c in line if c != "\n"])
    return out

def count_word(matrix: list[list], word) -> int:
    count = 0
    len_matrix = len(matrix)
    for i in range(len_matrix):
        for j in range(len_matrix):
            count += count_word_for_pos(matrix, (i,j), word)

    return count

def count_word_for_pos(matrix: list[list], pos: tuple[int, int], word: str) -> int:
    count = 0
    if pos[0] < 1 or pos[0] > len(matrix)-2 or pos[1] < 1 or pos[1] > len(matrix)-2:
        return 0
    patterns = [[(-1,-1),(1,-1),(0,0),(-1,1),(1,1)],
                [(1,1),(-1,1),(0,0),(1,-1),(-1,-1)],
                [(-1,-1),(-1,1),(0,0),(1,-1),(1,1)],
                [(1,1),(1,-1),(0,0),(-1,1),(-1,-1)],]
    for pattern in patterns:
        s = "".join([matrix[pos[0]+p[0]][pos[1]+p[1]] for p in pattern])
        if s == word:
            return 1

    return count

if __name__ == "__main__":
    main()