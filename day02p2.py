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
            pattern = ""
            for n in possible_id:
                pattern += n
                
                if len(pattern) * 2 > len(possible_id):
                    break
                
                if len(possible_id) % len(pattern) != 0:
                    continue
                
                if pattern * (len(possible_id) // len(pattern)) == possible_id:
                    total_invalid += int(possible_id)
                    break
                            
    print(total_invalid)
    
                


if __name__ == "__main__":
    main()
