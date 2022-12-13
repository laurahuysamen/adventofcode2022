import sys
import time
from functools import cmp_to_key

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
    print (pt1results)

    print ("PART 2 RESULTS:")
    print (pt2results)
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")

def is_in_right_order(first, second):
    #print(f"comparing `{first}` and `{second}`")
    if type(first) == int and type(second) == list:
        return is_in_right_order([first], second) 
    elif type(first) == list and type(second) == int:
        return is_in_right_order(first, [second])
    elif type(first) == int and type(second) == int:
        if int(first) < int(second):
            return True
        elif int(first) > int(second):
            return False
        else:
            return None
    elif type(first) == list and type(second) == list:

        for i in range(len(first)):
            if i < len(second):
                result = is_in_right_order(first[i], second[i])
                if result is not None:
                    return result
        if len(first) > len(second):
            return False
        elif len(first) < len(second):
            return True
        else:
            return None
    return None

def order_comparison(first, second):
    answer = is_in_right_order(first, second)
    if answer == None:
        return 0
    if answer:
        return -1
    else:
        return 1

def part1(filename):     
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        if count % 3 != 0:
            continue
        results.append(is_in_right_order(eval(line), eval(lines[count+1])))
        #print("----")
            
    result_sum = 0
    for count, result in enumerate(results):  
        #print(f"{count+1}: {result}")
        if result:
            result_sum = result_sum + count + 1
    return result_sum

def part2(filename):
    results = []

    lines = read_file(filename)
    lines.append("[[2]]")
    lines.append("[[6]]")
    lines = [eval(line) for line in lines if line != ""]
    
    results = sorted(lines, key=cmp_to_key(order_comparison))
    
    a = results.index([[2]])+1
    b = results.index([[6]])+1

    return a*b


if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)