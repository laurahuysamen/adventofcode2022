import sys
import time
import numpy as np
from collections import Counter
import itertools
from functools import reduce
import copy
import math
import uuid
import networkx as nx
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


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
    print(sum(pt1results))
    print ("PART 2 RESULTS:")
    for result in pt2results:
        print(result)   
    print(sum(pt2results))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []
    
    backpack_compartment1 = []
    backpack_compartment2 = []
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    lines = read_file(filename)
    for count, line in enumerate(lines):
        len(line)
        comp1 = line[0: int(len(line)/2)]
        comp2 = line[int(len(line)/2) : ]
        intersection = [l for l in comp1 if l in comp2]
        print(intersection[0])

        common_item = intersection[0]
        if common_item in lowercase:
            results.append(ord(common_item) - 96)
        else:
            results.append(ord(common_item) - 38)
           
    
    return results

def part2(filename):
    results = []

    rucksack = []

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    lines = read_file(filename)
    for count, line in enumerate(lines):
        rucksack.append(line)

        if ((count + 1) % 3 == 0):
            print(count)
            intersection = [l for l in rucksack[count] if (l in rucksack[count-1] and l in rucksack[count-2])]
            print(intersection[0])

            common_item = intersection[0]
            if common_item in lowercase:
                results.append(ord(common_item) - 96)
            else:
                results.append(ord(common_item) - 38)


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