import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()
    
    
    equations = list(zip(*[l.split() for l in puzzle_input.split("\n")]))
    
    total = 0
    for equation in equations:
        numbers = list(map(int, equation[:-1]))
        match equation[-1]:
            case "+":
                total += sum(numbers)
            case "*":
                product = 1
                for n in numbers:
                    product *= n
                total += product
            

    print(total)
    
if __name__ == "__main__":
    main()
