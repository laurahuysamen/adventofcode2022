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
    print (pt1results)

    print ("PART 2 RESULTS:")
    print (pt2results[0])  
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):  
    lines = read_file(filename)
    hills = np.array([[ord(l) for l in list(line)] for line in lines])
    me = None  #83
    goal = None #69
    num_rows, num_cols = hills.shape
    #build a graph
    pos = {}
    mygraph = nx.DiGraph()
    for x in range(0, num_rows): 
        for y in range(0, num_cols):
            if hills[x,y] == 83: #S
                me = [x,y]
                hills[x,y] = 97 #a
            if hills[x,y] == 69: #E
                goal = [x,y]
                hills[x,y] = 122 #z
            pos[f"{x}:{y}"] = (x,y)
            if x > 0:
                if hills[x,y] - hills[x-1, y] >= -1:
                    mygraph.add_edge(f"{x}:{y}", f"{x-1}:{y}") 
                if hills[x-1, y] - hills[x, y] >= -1:
                    mygraph.add_edge(f"{x-1}:{y}", f"{x}:{y}")
            if y > 0:
                if hills[x,y] - hills[x, y-1] >= -1:
                    mygraph.add_edge(f"{x}:{y}", f"{x}:{y-1}")
                if hills[x, y-1] - hills[x, y] >= -1:
                    mygraph.add_edge(f"{x}:{y-1}", f"{x}:{y}")

    length = nx.shortest_path_length(mygraph, f"{me[0]}:{me[1]}", f"{goal[0]}:{goal[1]}")

    # options = {"node_size" : 20}
    # nx.draw(mygraph, pos=pos, **options)
    # plt.axis("off")
    # plt.show()

    return length

def part2(filename):
    lines = read_file(filename)
    hills = np.array([[ord(l) for l in list(line)] for line in lines])

    starts = [] 
    goal = None #69

    num_rows, num_cols = hills.shape
    #build a graph
    pos = {}
    mygraph = nx.DiGraph()
    for x in range(0, num_rows): 
        for y in range(0, num_cols):
            if hills[x,y] == 83: #S
                hills[x,y] = 97 #a
            if hills[x,y] == 69: #E
                goal = [x,y]
                hills[x,y] = 122 #z

            if hills[x,y] == 97:
                starts.append([x,y])

            pos[f"{x}:{y}"] = (x,y)
            if x > 0:
                if hills[x,y] - hills[x-1, y] >= -1:
                    mygraph.add_edge(f"{x}:{y}", f"{x-1}:{y}") 
                if hills[x-1, y] - hills[x, y] >= -1:
                    mygraph.add_edge(f"{x-1}:{y}", f"{x}:{y}")
            if y > 0:
                if hills[x,y] - hills[x, y-1] >= -1:
                    mygraph.add_edge(f"{x}:{y}", f"{x}:{y-1}")
                if hills[x, y-1] - hills[x, y] >= -1:
                    mygraph.add_edge(f"{x}:{y-1}", f"{x}:{y}")

    lengths = []
    for start in starts:
        try:
            length =  nx.shortest_path_length(mygraph, f"{start[0]}:{start[1]}", f"{goal[0]}:{goal[1]}")
            lengths.append(length)
        except: #if there's no path don't worry about it
            continue
    lengths.sort()
    return lengths

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)