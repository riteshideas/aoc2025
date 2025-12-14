import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    points = [tuple(map(int, line.split(","))) for line in puzzle_input.split("\n")]
    points.sort(key=lambda pos: pos[0] ** 2 + pos[1] ** 2)
    p1, p2 = points[0], points[-1]
    print((p2[0] - p1[0] + 1) * (p2[1] - p1[1] + 1))

    
if __name__ == "__main__":
    main()
