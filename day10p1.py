import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    total_depth = 0
    for line in puzzle_input.split("\n"):
        manual = line.split(" ")

        # We are looping through the string from left so:
        # ...## is ##... so that least significant digit is at the right
        light_diagram = manual[0][1:-1]
        button_wiring = manual[1:-1]

        light_binary = 0
        for i, light in enumerate(light_diagram):
            if light == "#":
                light_binary |= 1 << i

        button_schematics = []

        for button in button_wiring:
            button_schematic = 0
            buttons_press = [*map(int, button[1:-1].split(","))]
            for button_press in buttons_press:
                button_schematic |= 1 << button_press

            button_schematics.append(button_schematic)

        button_toggle_states = [(0, 0)]  # initially everything is off
        searched = set()
        best_depth = float("inf")
        while True:
            button_toggle_states.sort(key=lambda b: b[0], reverse=True)
            curr_depth, curr_button = button_toggle_states.pop()
            if curr_button == light_binary:
                best_depth = curr_depth
                break

            if curr_button in searched:
                print("Something wrong", curr_button, searched)
            searched.add(curr_button)

            for button_config in button_schematics:
                new_button = curr_button ^ button_config

                if new_button in searched:
                    continue

                if new_button in [b for _, b in button_toggle_states]:
                    continue

                button_toggle_states.append((curr_depth + 1, new_button))

        total_depth += best_depth
        
    print(total_depth)


if __name__ == "__main__":
    main()
