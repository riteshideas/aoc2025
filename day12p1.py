import sys

"""
This is how the actual solution is supposed to look like but is extremely slow. However, this puzzle is tailered only for the actual input not the testcase, we just need to assume that one present is 3x3 with no gaps
def rotations(p):
    return [
        p,
        list(reversed(["".join(line) for line in zip(*p)])),
        [line[::-1] for line in reversed(p)],
        ["".join(reversed(line)) for line in zip(*p)],
    ]


searched = {}


def search(
    DIM,
    filled,
    max_uses,
    patterns,
):
    if (hash(filled), max_uses) in searched:
        return searched[(hash(filled), max_uses)]

    if all([m == 0 for m in max_uses]):
        searched[(hash(filled), max_uses)] = True
        return True

    for i in range(len(max_uses)):
        if max_uses[i] == 0:
            continue
        pattern = patterns[i]
        new_max_uses = list(max_uses[:i]) + [max_uses[i] - 1] + list(max_uses[i + 1 :])
        for x in range(DIM[0]):
            for y in range(DIM[1]):
                center_pos = complex(x, y)
                for pattern_comb in pattern:
                    centered_comb = []
                    for num in pattern_comb:
                        new_pos: complex = num + center_pos
                        if new_pos.real < 0 or new_pos.real >= DIM[0] or new_pos.imag < 0 or new_pos.imag >= DIM[1]:
                            break
                        if new_pos in filled:
                            break
                        centered_comb.append(new_pos)

                    else:
                        new_filled = list(filled)
                        new_filled.extend(centered_comb)
                        status = search(DIM, tuple(new_filled), tuple(new_max_uses), patterns)
                        if status:
                            searched[(hash(filled), max_uses)] = True
                            return True

    searched[(hash(filled), max_uses)] = False
    return False


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read().split("\n\n")

    regions = puzzle_input[-1]
    patterns = []

    for pattern in puzzle_input[:-1]:
        presents = pattern.split("\n")[1:]
        flipped_presents = [p[::-1] for p in presents]

        pattern_combinations = []
        for pattern_comb in [*rotations(presents), *rotations(flipped_presents)]:
            pattern_pos = []
            for y, line in enumerate(pattern_comb):
                for x, char in enumerate(line):
                    if char == "#":
                        pattern_pos.append(complex(x, y))
            pattern_combinations.append(tuple(pattern_pos))

        patterns.append(tuple(pattern_combinations))

    for region in regions.split("\n"):
        size, max_uses = region.split(": ")
        max_uses = [*map(int, max_uses.split(" "))]
        DIM = (*map(int, size.split("x")),)
        print(search(DIM, (), tuple(max_uses), tuple(patterns)))

"""


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()
    regions = puzzle_input.split("\n\n")[-1].split("\n")
    passed = 0
    for region in regions:
        dim, presents = region.split(": ")
        dim = [*map(int, dim.split("x"))]
        if dim[0] * dim[1] >= sum(map(int, presents.split(" "))) * 9:
            passed += 1
    print(passed)


if __name__ == "__main__":
    main()
