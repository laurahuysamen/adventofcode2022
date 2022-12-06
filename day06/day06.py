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
    for result in pt1results:
        print(result)   

    print ("PART 2 RESULTS:")
    for result in pt2results:
        print(result)   
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []
    lines = read_file(filename)[0]

    packet = list(lines[0:4])
    for count, line in enumerate(lines[4:]):
        if len(set(packet)) == 4:
            results.append(count + 4)
            break
        else:
            packet.pop(0)
            packet.append(line)

    return results

def part2(filename):
    results = []
    lines = read_file(filename)[0]

    packet = list(lines[0:14])
    for count, line in enumerate(lines[14:]):
        if len(set(packet)) == 14:
            results.append(count + 14)
            break
        else:
            packet.pop(0)
            packet.append(line)

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