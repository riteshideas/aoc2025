import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    paper_rolls = puzzle_input.split("\n")
    DIMS = (len(paper_rolls[0]), len(paper_rolls))

    DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

    accessible = 0
    for y in range(DIMS[1]):
        for x in range(DIMS[0]):
            if paper_rolls[y][x] != "@":
                continue

            adjacent = 0

            for paper_dir in DIRS:
                nearby = (paper_dir[0] + x, paper_dir[1] + y)
                if nearby[0] >= DIMS[0] or 0 > nearby[0] or nearby[1] >= DIMS[1] or 0 > nearby[1]:
                    continue

                if paper_rolls[nearby[1]][nearby[0]] == "@":
                    adjacent += 1

            if adjacent < 4:
                accessible += 1

    print(accessible)


if __name__ == "__main__":
    main()
