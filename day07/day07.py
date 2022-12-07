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
    # for result in pt1results:
    #     print(result)   
    print (sum(pt1results))

    print ("PART 2 RESULTS:")
    for result in pt2results:
        print(result)   
    #print (sum(pt2results))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):  
    filesystem = {}
    current_path = []
    directory_names = ["/"]
    lines = read_file(filename)

    for count, line in enumerate(lines):
        splitline = line.split(' ')
        if line.startswith("$ cd"): 
            new_dir = splitline[2]
            if new_dir == "..":
                current_path.pop()
            elif new_dir == "/":
                current_path = [""]
            else:
                current_path.append(new_dir)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            filesystem["/".join(current_path) + "/" + splitline[1]] = 0
            directory_names.append("/".join(current_path) + "/" + splitline[1])
        else:
            filesystem["/".join(current_path) + "/" + splitline[1]] = splitline[0]
            continue
        continue

    #now evaluate the filesystem
    directory_sizes = []
    for directory in directory_names:
        contents = []
        for key in filesystem:
            if key.startswith(directory):
                contents.append(filesystem[key])
        directory_sizes.append(sum([int(d) for d in contents]))

    filtered_sizes = [d for d in directory_sizes if d < 100000]


    return filtered_sizes

def part2(filename):
    filesystem = {}
    current_path = []
    directory_names = ["/"]
    lines = read_file(filename)

    for count, line in enumerate(lines):
        splitline = line.split(' ')
        if line.startswith("$ cd"): 
            new_dir = splitline[2]
            if new_dir == "..":
                current_path.pop()
            elif new_dir == "/":
                current_path = [""]
            else:
                current_path.append(new_dir)
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir"):
            filesystem["/".join(current_path) + "/" + splitline[1]] = 0
            directory_names.append("/".join(current_path) + "/" + splitline[1])
        else:
            filesystem["/".join(current_path) + "/" + splitline[1]] = splitline[0]
            continue
        continue

    #now evaluate the filesystem
    directory_sizes = []
    for directory in directory_names:
        contents = []
        for key in filesystem:
            if key.startswith(directory):
                contents.append(filesystem[key])
        directory_sizes.append(sum([int(d) for d in contents]))

    current_space = 70000000 - directory_sizes[0] #first one is the root directory
    required_space = 30000000
    needed_space = required_space - current_space

    filtered_sizes = [d for d in directory_sizes if d >= needed_space]
    filtered_sizes.sort()
    return [filtered_sizes[0]]

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)
