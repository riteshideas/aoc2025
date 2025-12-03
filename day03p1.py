import sys

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
        highest_bank_volt = 0
        for i in range(len(bank)):
            tenths = bank[i]
            
            if highest_bank_volt // 10 > int(tenths):
                continue
            
            for j in range(i+1, len(bank)):
                ones = bank[j]
                highest_bank_volt = max(highest_bank_volt, int(tenths) * 10 + int(ones))
                
        max_volt += highest_bank_volt
        
    print(max_volt)
    

    
if __name__ == "__main__":
    main()
