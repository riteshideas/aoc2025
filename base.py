import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    
if __name__ == "__main__":
    main()
