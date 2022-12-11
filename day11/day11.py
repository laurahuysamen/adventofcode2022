import sys
import time
import numpy as np
import copy

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
    print (pt1results[0]*pt1results[1])

    print ("PART 2 RESULTS:")
    print (pt2results[0]*pt2results[1])
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
      
class Monkey():

    def __init__(self, items, operation, divisible_by_test, true_monkey, false_monkey):
        self.items = items
        self.operation = operation
        self.divisible_by_test = divisible_by_test
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0

    def to_string(self):
        return f'{self.items}, op: {self.operation}, div: {self.divisible_by_test} ? {self.true_monkey} : {self.false_monkey} | inspections: {self.inspections}'

def part1(filename):     
    results = []
    monkeys = []
    lines = read_file(filename)
    index = 0

    while index < len(lines):
        if lines[index].startswith("Monkey"):
            items = [int(item) for item in lines[index + 1].split(":")[1].split(",")]
            operation = lines[index + 2].split("=")[1]
            test = int(lines[index + 3].split(" ")[3])
            true_monkey = int(lines[index + 4].split(" ")[5])
            false_monkey = int(lines[index + 5].split(" ")[5]) 
            monkeys.append(Monkey(items, operation, test, true_monkey, false_monkey))
            index = index + 7

    for round in range(20):
        for monkey in monkeys: 
            current_monkey_list = copy.copy(monkey.items)
            for old in monkey.items:
                current_monkey_list.pop(0)
                monkey.inspections = monkey.inspections + 1

                worry_level = eval(monkey.operation) #old gets used here
                worry_level = worry_level // 3
                if (worry_level % monkey.divisible_by_test == 0):
                    monkeys[monkey.true_monkey].items.append(worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(worry_level)  
            monkey.items = current_monkey_list

        # for result in monkeys:
        #     print(result.to_string())   
        # print("-------")
        
    results = [monkey.inspections for monkey in monkeys]
    results.sort()
    
    return list(reversed(results))

def part2(filename):
    results = []
    monkeys = []
    lines = read_file(filename)
    index = 0

    while index < len(lines):
        if lines[index].startswith("Monkey"):
            items = [int(item) for item in lines[index + 1].split(":")[1].split(",")]
            operation = lines[index + 2].split("=")[1]
            test = int(lines[index + 3].split(" ")[3])
            true_monkey = int(lines[index + 4].split(" ")[5])
            false_monkey = int(lines[index + 5].split(" ")[5]) 
            monkeys.append(Monkey(items, operation, test, true_monkey, false_monkey))
            index = index + 7

    largest_common_divisor = int(np.prod([monkey.divisible_by_test for monkey in monkeys]))
   
    for round in range(10000):
        for monkey in monkeys: 
            current_monkey_list = copy.copy(monkey.items)
            for old in monkey.items:
                current_monkey_list.pop(0)
                monkey.inspections = monkey.inspections + 1
                worry_level = eval(monkey.operation) #old gets used here

                worry_level = (worry_level % largest_common_divisor)

                if (worry_level % monkey.divisible_by_test == 0):
                    monkeys[monkey.true_monkey].items.append(worry_level)
                else:
                    monkeys[monkey.false_monkey].items.append(worry_level)  
            monkey.items = current_monkey_list
        #if (round % 1000 == 0):
            # print(f"---ROUND {round}----")
            # for result in monkeys:
            #     print(result.to_string())   
        
    results = [monkey.inspections for monkey in monkeys]
    results.sort()
    
    return list(reversed(results))

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)

