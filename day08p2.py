import sys

def dist(p1, p2):
    """Euclidean distance between two points"""
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    dz = p1[2] - p2[2]
    return (dx * dx + dy * dy + dz * dz)

def main():
    input_file = "testcase.txt" if len(sys.argv) < 2 else sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    points = [tuple(map(int, pos.split(","))) for pos in puzzle_input.split()]
    circuits = {i: {pos} for i, pos in enumerate(points)}
    junction_box_to_circuit = {pos: i for i, pos in enumerate(points)}
    
    distances = []
    for k, p_1 in enumerate(points):

        for j in range(k, len(points)):
            p_2 = points[j]
            if p_1 == p_2:
                continue
            d = dist(p_1, p_2)

            distances.append((d, p_1, p_2))
                

    distances.sort()
    best_distances = distances[:]

    for distance in best_distances:
        _, p1, p2 = distance
        p1_circuit = junction_box_to_circuit[p1]
        p2_circuit = junction_box_to_circuit[p2]
        combined_circuit = circuits[p1_circuit] | circuits[p2_circuit]

        del circuits[p1_circuit]
        if p1_circuit != p2_circuit:
            del circuits[p2_circuit]

        circuit_id = id(combined_circuit)
        circuits[circuit_id] = combined_circuit
        
        for junction_box in combined_circuit:
            junction_box_to_circuit[junction_box] = circuit_id

        best_circuits = [len(c) for c in circuits.values()]
        
        if len(best_circuits) == 1:
            print(p1[0] * p2[0])
            break

        
    

if __name__ == "__main__":
    main()
