import sys


def volt_search(complete_bank, remaining_bank, current_volts, max_depth):
    if len(current_volts) == max_depth:
        return int(current_volts)

    assert len(current_volts) < max_depth, f"{complete_bank}, {remaining_bank}, {current_volts}, {max_depth}"

    volts_required = max_depth - len(current_volts)

    next_volts = []

    for j in range((len(remaining_bank) - volts_required) + 1):
        next_volts.append((j, remaining_bank[j]))

    # Sort by the highest volt, then sort by the lowest the J index
    best_next_volt = sorted(next_volts, key=lambda v: (int(v[1]), -v[0]), reverse=True)
    next_volt = best_next_volt[0]

    return volt_search(complete_bank, remaining_bank[next_volt[0] + 1 :], current_volts + next_volt[1], max_depth)


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
        max_volt += volt_search(bank, bank, "", 12)

    print(max_volt)


if __name__ == "__main__":
    main()
