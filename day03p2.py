import sys
from functools import cache


@cache
def volt_dfs(complete_bank, remaining_bank, current_volts, max_depth):
    if len(current_volts) == max_depth:
        return int(current_volts)

    assert len(current_volts) < max_depth, f"{complete_bank}, {remaining_bank}, {current_volts}, {max_depth}"

    volts_required = max_depth - len(current_volts)
    
    highest_volt = 0
    
    next_volts = []
    
    for j in range((len(remaining_bank) - volts_required) + 1):
        next_volts.append((j, remaining_bank[j]))

    max_next_volt = max(next_volts, key=lambda v: int(v[1]))[1]
    
    for j, next_volt in next_volts:
        if next_volt != max_next_volt:
            continue
        
        possible_highest_volt = volt_dfs(complete_bank, remaining_bank[j+1:], current_volts + next_volt, max_depth)
        highest_volt = max(possible_highest_volt, highest_volt)
        
    return highest_volt



def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    max_volt = 0
    banks = puzzle_input.split("\n")
    for bank in banks:
        max_volt += volt_dfs(bank, bank, "", 12)
        volt_dfs.cache_clear()

    print(max_volt)


if __name__ == "__main__":
    main()