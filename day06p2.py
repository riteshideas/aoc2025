import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    vertical_equations = puzzle_input.split("\n")

    operators = vertical_equations[-1]
    total = 0

    equations_split_index = []
    empty_spaces = []
    for i, operator in enumerate(operators):
        if operator == " ":
            continue

        equations_split_index.append(i)
        if i > 0:
            empty_spaces.append(i - 1)

    equations_split_index.append(len(operators))

    for j in range(len(equations_split_index) - 1):

        prev_split_index, split_index = equations_split_index[j : j + 2]
        curr_vert_equation = []

        for vertical_equation in vertical_equations[:-1]:
            curr_vert_equation.append(
                vertical_equation[prev_split_index : split_index - (1 if j != len(equations_split_index) - 2 else 0)]
            )

        equation = [int("".join(num)) for num in zip(*map(list, curr_vert_equation))]
        
        match operators[prev_split_index]:
            case "*":
                product = 1
                for num in equation:
                    product *= num
                total += product
            case "+":
                total += sum(equation)
    
    print(total)
                    

if __name__ == "__main__":
    main()
