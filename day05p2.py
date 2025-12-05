import sys


def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    fresh_ingredients_raw, _ = puzzle_input.split("\n\n")

    fresh_ingredients = []

    for ingredient in fresh_ingredients_raw.split("\n"):
        i_range = tuple(sorted(map(int, ingredient.split("-"))))

        conflicting = []
        for i, fresh_ingredient in enumerate(fresh_ingredients):
            # Has any conflicts
            if fresh_ingredient[0] <= i_range[1] and i_range[0] <= fresh_ingredient[1]:
                conflicting.append(i)

        # Remove the highest index
        new_fresh_ingredient = i_range
        for i in sorted(conflicting, reverse=True):
            new_fresh_ingredient = (
                min(new_fresh_ingredient[0], fresh_ingredients[i][0]),
                max(new_fresh_ingredient[1], fresh_ingredients[i][1]),
            )
            fresh_ingredients.pop(i)

        fresh_ingredients.append(new_fresh_ingredient)

    print(sum([e - s + 1 for s, e in fresh_ingredients]))


if __name__ == "__main__":
    main()
