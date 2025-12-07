import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    grid = []
    start = None
    splitters_hit = {}
    height = 0
    width = 0

    for y, line in enumerate(puzzle_input.split("\n")):
        grid.append(line)
        height = max(height, y + 1)
        for x, char in enumerate(line):
            width = max(width, x + 1)
            coord = complex(x, y)
            if char == "S":
                start = coord
            elif char == "^":
                splitters_hit[coord] = 0

    assert start, "Start not found"

    # Start from the bottom and work the way up
    beams = [(1, complex(x, height - 1)) for x in range(width)]

    for _ in range(height-1):
        temp_new_beams = set()
        new_beams = []
        for timelines_len, beam in beams:
            new_beam = beam - 1j
            if new_beam in splitters_hit:
                continue

            for possible_splitter in (new_beam + 1, new_beam - 1):
                if possible_splitter in splitters_hit:
                    splitters_hit[possible_splitter] += timelines_len
                    temp_new_beams.add(possible_splitter)
            
            new_beams.append((timelines_len, new_beam))
        
        for beam in temp_new_beams:
            new_beams.append((splitters_hit[beam], beam))
        beams = new_beams[:]

    print([timeline for timeline, beam_pos in beams if beam_pos == start][0])

if __name__ == "__main__":
    main()
