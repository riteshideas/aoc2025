import sys
from collections import deque

"""

Coordinates Compression

"""

def main():
    if len(sys.argv) < 2:
        input_file = "testcase.txt"
    else:
        input_file = sys.argv[1]

    # Read the input exactly as received.
    with open(input_file, "r") as f:
        puzzle_input = f.read()

    points = [(*map(int, line.split(",")), i) for i, line in enumerate(puzzle_input.split("\n"))]

    compressed_coords_dict = {}

    # For X coord
    points.sort(key=lambda pos: pos[0])
    prev_compressed_x = (0, 0)  # compressed, actual
    for x, _, i in points:
        if prev_compressed_x[1] != x:
            prev_compressed_x = (prev_compressed_x[0] + 2, x)
        compressed_coords_dict[i] = (prev_compressed_x[0], None)

    # For Y coord
    points.sort(key=lambda pos: pos[1])
    prev_compressed_y = (0, 0)  # compressed, actual

    for _, y, i in points:
        if prev_compressed_y[1] != y:
            prev_compressed_y = (prev_compressed_y[0] + 2, y)
        compressed_coords_dict[i] = (compressed_coords_dict[i][0], prev_compressed_y[0])

    compressed_coords = [(*compressed_coords_dict[i], i) for i in compressed_coords_dict]
    compressed_coords.sort(key=lambda pos: pos[2])
    compressed_edges = [(compressed_coords[j], compressed_coords[j + 1]) for j in range(-1, len(compressed_coords) - 1)]

    edges_pos = set()
    for start, end in compressed_edges:
        if start[0] == end[0]:
            s = min(start[1], end[1])
            e = max(start[1], end[1])

            for y in range(s, e + 1):
                edges_pos.add((start[0], y))
        elif start[1] == end[1]:
            s = min(start[0], end[0])
            e = max(start[0], end[0])

            for x in range(s, e + 1):
                edges_pos.add((x, start[1]))
        else:
            print(start, end)

    DIMS = (prev_compressed_x[0] + 1, prev_compressed_y[0] + 1)
    outside = {(0, 0)}
    queue = deque(outside)

    while len(queue):
        curr = queue.popleft()

        for adj_dir in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            adj_node = (curr[0] + adj_dir[0], curr[1] + adj_dir[1])
            if adj_node[0] < 0 or adj_node[0] > DIMS[0] or adj_node[1] < 0 or adj_node[1] > DIMS[1]:
                continue
            if adj_node in edges_pos:
                continue
            if adj_node in outside:
                continue
            outside.add(adj_node)
            queue.append(adj_node)


    # Sort by the index
    points.sort(key=lambda pos: pos[2])
    compressed_coords.sort(key=lambda pos: pos[2])
    POINTS_LEN = len(compressed_coords)  # should be same as len(points)

    max_area = -float("inf")
    for i in range(POINTS_LEN):
        p1_x, p1_y, _ = compressed_coords[i]
        for j in range(i + 1, POINTS_LEN):
            p2_x, p2_y, _ = compressed_coords[j]

            area = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)

            if area < max_area:
                continue

            t_x = min(p1_x, p2_x)
            t_y = min(p1_y, p2_y)

            b_x = max(p1_x, p2_x)
            b_y = max(p1_y, p2_y)

            rectangle = [(t_x, t_y), (b_x, t_y), (b_x, b_y), (t_x, b_y)]

            invalid = False
            for h in range(-1, 3):
                start, end = rectangle[h], rectangle[h + 1]
                pos_range = None
                if start[0] == end[0]:
                    s = min(start[1], end[1])
                    e = max(start[1], end[1])
                    pos_range = range(s, e + 1)

                elif start[1] == end[1]:
                    s = min(start[0], end[0])
                    e = max(start[0], end[0])
                    pos_range = range(s, e + 1)
                
                for delta_pos in pos_range:
                    pos = (start[0] if start[0] == end[0] else delta_pos, start[1] if start[1] == end[1] else delta_pos)
                    if pos in outside:
                        invalid = True
                        break

                if invalid:
                    break

            if invalid:
                continue

            max_area = area
    print(max_area)


if __name__ == "__main__":
    main()
