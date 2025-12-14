import sys
from functools import cache

"""

Multiple ways to solve this:

1. using gauss jordan elimination (https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/)
2. Using Z3 (https://microsoft.github.io/z3guide/docs/logic/intro/)
3. Bifurcate (https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/) < Im using this method

101 (5) (0, 2)
"""


@cache
def search(volatages, button_combinations):
    if sum(volatages) == 0:
        return 0

    target = 0
    for i, v in enumerate(volatages):
        target |= (v % 2) << i

    # print("target", bin(target)[2:], volatages)

    voltage_len = len(volatages)
    best_cost = float("inf")

    for i, (combination_result, button_combination) in enumerate(button_combinations):
        if combination_result == target:
            combination_len = bin(i)[2:].count("1")

            new_volt = list(volatages)
            for i in button_combination:
                for j in range(voltage_len):
                    new_volt[j] -= (i >> j) & 1

            if min(new_volt) < 0:
                continue

            new_volt = tuple([v // 2 for v in new_volt])
            cost = 2 * search(new_volt, button_combinations) + combination_len
            best_cost = min(cost, best_cost)

    return best_cost


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    total_cost = 0
    total_len = len(puzzle_input.split("\n"))
    for i, line in enumerate(puzzle_input.split("\n")):
        print(f"{(i + 1) / total_len * 100:.2f}%", end="\r")
        manual = line.split(" ")

        # volatages: (1, 4, 0) -> Increases the volatages for the index 0, 1, 4
        # Counters (0, 0, 0, 0) result: {1, 5, 3, 5} -> We wll have to reverse this into (5, 3, 5, 1)
        #

        light_diagram = manual[0][1:-1]
        button_wiring = manual[1:-1]
        target_volatges = [*map(int, manual[-1][1:-1].split(","))]

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

        button_schematics_len = len(button_schematics)

        button_combinations = []
        for i in range(2**button_schematics_len):
            combination_result = 0
            button_combination = []
            for j in range(button_schematics_len):
                if (i >> j) & 1:
                    combination_result ^= button_schematics[j]
                    button_combination.append(button_schematics[j])
            button_combinations.append((combination_result, tuple(button_combination)))

        cost = search(tuple(target_volatges), tuple(button_combinations))
        total_cost += cost
        search.cache_clear()

    print("\n\n", total_cost)


if __name__ == "__main__":
    main()
