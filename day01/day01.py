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
    lines = read_file(filename)
    most_calorie_elf = 0
    latest_elf = 0
    for count, line in enumerate(lines):
        if line == "":            
            if latest_elf > most_calorie_elf:
                most_calorie_elf = latest_elf
            latest_elf = 0                        
        else:
            latest_elf += int(line) 

    results.append(most_calorie_elf)
    return results

def part2(filename):
    
    results = []
    lines = read_file(filename)
    latest_elf = 0
    for count, line in enumerate(lines):
        if line == "":          
            results.append(latest_elf) 
            latest_elf = 0                        
        else:
            latest_elf += int(line) 

    results.sort(reverse=True)

    return [sum(results[0:3])]

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)