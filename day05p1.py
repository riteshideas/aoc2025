import sys

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]
    
    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()
    
    fresh_ingredients_raw, available_ingredients = puzzle_input.split("\n\n")
    
    fresh_ingredients = []
    fresh_ingredients_num = 0
    for ingredient in fresh_ingredients_raw.split("\n"):
        i_range = map(int, ingredient.split("-"))
        fresh_ingredients.append(tuple(i_range))
        
    for ingredient in available_ingredients.split("\n"):
        check_ingredient = int(ingredient)
        
        # See if its in the range
        for fresh_ingredient in fresh_ingredients:
            if fresh_ingredient[0] <= check_ingredient <= fresh_ingredient[1]:
                break
        else:
            continue
        
        fresh_ingredients_num += 1
        
    print(fresh_ingredients_num)
            

    
if __name__ == "__main__":
    main()
