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

    print ("PART 2 RESULTS:")
    for result in pt2results:
        print(result)   
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        continue

    return results

def part2(filename):
    results = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        continue

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