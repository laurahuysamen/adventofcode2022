import sys
import time


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

    print ("PART 1 RESULTS:")
    print (sum(pt1results))

    print ("PART 2 RESULTS:") 
    print (sum(pt2results))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        pairs = line.split(",")
        range1 = [int(i) for i in pairs[0].split("-")]  
        range2 = [int(i) for i in pairs[1].split("-")]  

        if range1[0] >= range2[0] and range1[1] <= range2[1]:
            results.append(1)
        elif range2[0] >= range1[0] and range2[1] <= range1[1]:    
            results.append(1)

    return results

def part2(filename):
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        pairs = line.split(",")
        range1 = [int(i) for i in pairs[0].split("-")]
        range2 = [int(i) for i in pairs[1].split("-")]

        list1 = range(range1[0],range1[1] + 1)
        list2 = range(range2[0],range2[1] + 1)

        combined = [l for l in list1 if l in list2]
        if len(combined) > 0:
            results.append(1)

    return results

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)