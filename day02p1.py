import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    ids = [map(int, id.split("-")) for id in puzzle_input.split(",")]

    total_invalid = 0
    for start_id, last_id in ids:
        for possible_id in range(start_id, last_id + 1):
            possible_id = str(possible_id)
            if len(possible_id) % 2 != 0:
                continue

            if possible_id[:len(possible_id) // 2] == possible_id[len(possible_id) // 2:]:
                total_invalid += int(possible_id)
                
    print(total_invalid)
    
                


if __name__ == "__main__":
    main()
