import sys
import time


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    lines = [str(l) for l in lines]
    return lines

def main(filename):
    print("PART 1:")
    start = time.time()
    pt1results = part1(filename)
    middle = time.time()
    print("PART 2:")
    pt2results = part2(filename)
    end = time.time() 

    print ("PART 1 RESULTS:")
    print("".join([column[-1] for column in pt1results if len(column) > 0]))

    print ("PART 2 RESULTS:")
    print("".join([column[-1] for column in pt2results if len(column) > 0]))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    columns = [[],[],[],[],[],[],[],[],[],[]]

    instructions = False

    lines = read_file(filename)
    for count, line in enumerate(lines):
        if line.startswith(" 1"):
            instructions = True
            columns = [list(reversed(column)) for column in columns]
            columns = [[c for c in column if c != " "] for column in columns]
            continue
        if line == "\n":
            continue

        # first set up the stacks
        if not instructions:
            if len(line) != 1:
                for i in range(int(len(line) / 4)):
                    columns[i].append(line[i*4 + 1])
        # then run the instructions
        else:
            line_detail = line.strip().split(" ")
            number_of_boxes = int(line_detail[1])
            starting_location = int(line_detail[3])
            ending_location = int(line_detail[5])

            for i in range(number_of_boxes):
                box = columns[starting_location - 1].pop()
                columns[ending_location - 1].append(box)

    return columns

def part2(filename):
    results = []

    columns = [[],[],[],[],[],[],[],[],[],[]]

    instructions = False

    lines = read_file(filename)
    for count, line in enumerate(lines):
        if line.startswith(" 1"):
            instructions = True
            columns = [list(reversed(column)) for column in columns]
            columns = [[c for c in column if c != " "] for column in columns]
            continue
        if line == "\n":
            continue

        # first set up the stacks
        if not instructions:
            if len(line) != 1:
                for i in range(int(len(line) / 4)):
                    columns[i].append(line[i*4 + 1])
        # then run the instructions
        else:
            line_detail = line.strip().split(" ")
            number_of_boxes = int(line_detail[1])
            starting_location = int(line_detail[3])
            ending_location = int(line_detail[5])

            boxes = []
            for i in range(number_of_boxes):
                boxes.append(columns[starting_location - 1].pop())
            boxes.reverse()
            columns[ending_location - 1].extend(boxes)

    return columns

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)