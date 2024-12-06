FNAME = "data.txt"
WORD = 'XMAS'


def main():
    matrix = file_to_matrix(FNAME)
    print(count_word(matrix, WORD))


def file_to_matrix(fname: str) -> list[list]:
    out = []
    fopen = open(fname, "r")
    for line in fopen:
        out.append([c for c in line if c != "\n"])
    return out


def count_word(matrix: list[list], word: str) -> int:
    count = 0
    len_matrix = len(matrix)
    for i in range(len_matrix):
        for j in range(len_matrix):
            count += count_word_for_pos(matrix, (i,j), WORD)

    return count


def count_word_for_pos(matrix: list[list], pos: tuple[int, int], word: str) -> int:
    directions = [(0,1), (0,-1), (1,0), (-1,0),
                  (1,1), (1,-1), (-1,1), (-1,-1)]
    count = 0
    len_word = len(word)
    for direction in directions:
        if get_word(matrix, pos, direction, len_word) == word:
            count += 1

    return count


def get_word(matrix: list[list], pos: tuple[int, int], direction: tuple[int, int], len_word: int) -> str:
    len_matrix = len(matrix)
    if (pos[0] + direction[0] * len_word < -1 or
        pos[0] + direction[0] * len_word > len_matrix or
        pos[1] + direction[1] * len_word < -1 or
        pos[1] + direction[1] * len_word > len_matrix):
        return ''
    
    return ''.join([matrix[pos[0]+i*direction[0]][pos[1]+i*direction[1]] for i in range(len_word)])

if __name__ == "__main__":
    main()