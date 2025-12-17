import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()
        
    paths = {}
    
    for line in puzzle_input.split("\n"):
        start, outputs = line.split(": ")
        paths[start] = outputs.split(" ")
    
    possible_paths = 0
    open_nodes = ["you"]
    while open_nodes:
        current_node = open_nodes.pop()
        if current_node == "out":
            possible_paths += 1
            continue
        open_nodes.extend(paths[current_node])
        
    print(possible_paths)
    
if __name__ == "__main__":
    main()
