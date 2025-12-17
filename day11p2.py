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

    def from_to(src, target, exclude):
        leading_paths = {}
        open_nodes = [(src, [src])]

        while open_nodes:
            current_node, path = open_nodes.pop()

            if current_node == target:
                for node in path:
                    leading_paths[node] = leading_paths.get(node, 0) + 1
                continue

            if current_node in exclude:
                continue

            for neighbour in paths[current_node]:
                if neighbour in leading_paths:
                    for node in path:
                        leading_paths[node] = leading_paths.get(node, 0) + leading_paths[neighbour]
                    continue

                open_nodes.append((neighbour, path[:] + [neighbour]))

        return leading_paths


    """
    
    IMPORTANT NOTE:
    
    This scenario only covers for path going from:
        svr -> fft -> dac -> out
    
    We go from the back eg dac -> out then fft -> dac since the nodes sea
    """

    dac_to_out = from_to("dac", "out", ["fft"])
    print(f"{dac_to_out['dac']=}")

    fft_to_dac = from_to("fft", "dac", list(dac_to_out) + ["out"])
    print(f"{fft_to_dac['fft']=}")


    svr_to_fft = from_to("svr", "fft", list(fft_to_dac) + ["dac", "out"])
    print(f"{svr_to_fft['svr']=}")
    
    print(svr_to_fft["svr"] * fft_to_dac["fft"] * dac_to_out["dac"])


if __name__ == "__main__":
    main()
