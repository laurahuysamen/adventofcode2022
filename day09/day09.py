import sys
import time
import numpy as np

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [str(l.strip()) for l in lines]
    return lines


def main(filename):
    print("PART 1:")
    start = time.time()
    pt1results = part1(filename)
    middle = time.time()
    print("PART 2:")
    pt2results = part2(filename)
    end = time.time()

    print("PART 1 RESULTS:")
    for result in pt1results:
        print(result)

    print("PART 2 RESULTS:")
    for result in pt2results:
        print(result)

    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")


def xDiff(head_pos, tail_pos):
    return head_pos[0] - tail_pos[0]


def yDiff(head_pos, tail_pos):
    return head_pos[1] - tail_pos[1]


def isAdjacent(head_pos, tail_pos):
    return (abs(xDiff(head_pos, tail_pos)) <= 1 and abs(yDiff(head_pos, tail_pos)) <= 1)


def part1(filename):
    size = 1000
    start = 500

    grid = np.zeros((size, size))
    # zero means it hasn't been visited by the tail.
    # mark startpoint
    grid[start, start] = 1

    head_position = [start, start]
    tail_position = [start, start]

    lines = read_file(filename)
    for _, line in enumerate(lines):
        splitline = line.split(" ")
        for _ in range(0, int(splitline[1])):
            if splitline[0] == "R":  # going Right, +y
                head_position[1] = head_position[1] + 1
            elif splitline[0] == "L":  # going Left -y
                head_position[1] = head_position[1] - 1
            elif splitline[0] == "U":  # going Up, -x
                head_position[0] = head_position[0] - 1
            elif splitline[0] == "D":  # going Down +x
                head_position[0] = head_position[0] + 1
            else:
                print("oh dear")

            if not isAdjacent(head_position, tail_position):
                # move the tail towards the head.

                # there are 8 possible directions the tail might need to move

                # let's handle the gridlines first
                xdelta = xDiff(head_position, tail_position)
                ydelta = yDiff(head_position, tail_position)

                if xdelta == 0:  # same horizontal
                    if ydelta > 1:
                        tail_position[1] = tail_position[1] + 1
                    elif ydelta < -1:
                        tail_position[1] = tail_position[1] - 1

                elif ydelta == 0:  # same vertical
                    if xdelta > 1:
                        tail_position[0] = tail_position[0] + 1
                    elif xdelta < -1:
                        tail_position[0] = tail_position[0] - 1

                # handle the 4 diagonals separately
                elif (xdelta > 1 and ydelta > 0) or (xdelta > 0 and ydelta > 1):
                    tail_position[0] = tail_position[0] + 1
                    tail_position[1] = tail_position[1] + 1
                elif (xdelta < -1 and ydelta > 0) or (xdelta < 0 and ydelta > 1):
                    tail_position[0] = tail_position[0] - 1
                    tail_position[1] = tail_position[1] + 1
                elif (xdelta > 1 and ydelta < 0) or (xdelta > 0 and ydelta < -1):
                    tail_position[0] = tail_position[0] + 1
                    tail_position[1] = tail_position[1] - 1
                elif (xdelta < -1 and ydelta < 0) or (xdelta < 0 and ydelta < -1):
                    tail_position[0] = tail_position[0] - 1
                    tail_position[1] = tail_position[1] - 1

                grid[tail_position[0], tail_position[1]] = 1
           # print(f"{splitline[0]}! Head: {head_position}, Tail: {tail_position}")

    return [int(sum(sum(grid)))]


def part2(filename):
    size = 1000
    start = 500

    grid = np.zeros((size, size))
    # zero means it hasn't been visited by the tail.
    # mark startpoint
    grid[start, start] = 1

    rope_positions = [[start, start] for i in range(10)]

    lines = read_file(filename)
    for _, line in enumerate(lines):
        splitline = line.split(" ")
        for _ in range(0, int(splitline[1])):
            if splitline[0] == "R":  # going Right, +y
                rope_positions[0][1] = rope_positions[0][1] + 1
            elif splitline[0] == "L":  # going Left -y
                rope_positions[0][1] = rope_positions[0][1] - 1
            elif splitline[0] == "U":  # going Up, -x
                rope_positions[0][0] = rope_positions[0][0] - 1
            elif splitline[0] == "D":  # going Down +x
                rope_positions[0][0] = rope_positions[0][0] + 1
            else:
                print("oh dear")

            for i in range(1, len(rope_positions)):
                if not isAdjacent(rope_positions[i-1], rope_positions[i]):
                    # move the tail towards the head.

                    # there are 8 possible directions the tail might need to move

                    # let's handle the gridlines first
                    xdelta = xDiff(rope_positions[i-1],  rope_positions[i])
                    ydelta = yDiff(rope_positions[i-1],  rope_positions[i])

                    if xdelta == 0:  # same horizontal
                        if ydelta > 1:
                            rope_positions[i][1] = rope_positions[i][1] + 1
                        elif ydelta < -1:
                            rope_positions[i][1] = rope_positions[i][1] - 1

                    elif ydelta == 0:  # same vertical
                        if xdelta > 1:
                            rope_positions[i][0] = rope_positions[i][0] + 1
                        elif xdelta < -1:
                            rope_positions[i][0] = rope_positions[i][0] - 1

                    # handle the 4 diagonals separately
                    elif (xdelta > 1 and ydelta > 0) or (xdelta > 0 and ydelta > 1):
                        rope_positions[i][0] = rope_positions[i][0] + 1
                        rope_positions[i][1] = rope_positions[i][1] + 1
                    elif (xdelta < -1 and ydelta > 0) or (xdelta < 0 and ydelta > 1):
                        rope_positions[i][0] = rope_positions[i][0] - 1
                        rope_positions[i][1] = rope_positions[i][1] + 1
                    elif (xdelta > 1 and ydelta < 0) or (xdelta > 0 and ydelta < -1):
                        rope_positions[i][0] = rope_positions[i][0] + 1
                        rope_positions[i][1] = rope_positions[i][1] - 1
                    elif (xdelta < -1 and ydelta < 0) or (xdelta < 0 and ydelta < -1):
                        rope_positions[i][0] = rope_positions[i][0] - 1
                        rope_positions[i][1] = rope_positions[i][1] - 1

                grid[rope_positions[-1][0],  rope_positions[-1][1]] = 1
            # print(f"{splitline[0]}! Head: {rope_positions[i-1]}, Tail: {rope_positions[i]}")

    return [int(sum(sum(grid)))]


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    # filename =
    main(filename)
