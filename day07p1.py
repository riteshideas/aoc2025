import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    start = None
    splitters = []
    height = 0

    for y, line in enumerate(puzzle_input.split("\n")):
        height = max(height, y + 1)
        for x, char in enumerate(line):
            coord = complex(x, y)
            if char == "S":
                start = coord
            elif char == "^":
                splitters.append(coord)

    assert start, "Start not found"
    beams = [start]
    hits = 0

    for _ in range(height):
        new_beams = set()
        for beam in beams:
            new_beam = beam + 1j
            if new_beam in splitters:
                hits += 1
                new_beams = new_beams.union({new_beam - 1, new_beam + 1})
            else:
                new_beams.add(new_beam)

        beams = list(new_beams)

    print(hits)


if __name__ == "__main__":
    main()
