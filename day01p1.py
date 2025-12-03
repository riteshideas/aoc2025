import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    data = puzzle_input.split()
        
    dial = 50
    dial_zeros = 0

    for turn in data:
        turn_type, turn_len = turn[0], int(turn[1:])
        move_dist = (["L", "R"].index(turn_type) * 2 - 1) * turn_len
        dial += move_dist
        dial = dial % 100
        if dial == 0:
            dial_zeros += 1

    print(dial_zeros)
    
if __name__ == "__main__":
    main()
