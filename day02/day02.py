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
    #for result in pt1results:
    #    print(result)   
    print (sum(pt1results))
    print ("PART 2 RESULTS:")
    #for result in pt2results:
    #    print(result)   
    print (sum(pt2results))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    rock = "A"
    paper = "B"
    scissors = "C"

    rock2 = "X"
    paper2 = "Y"
    scissors2 = "Z"

    win = 6
    draw = 3
    loss = 0

    rock_points = 1
    paper_points = 2
    scissors_points = 3

    lines = read_file(filename)
    for count, line in enumerate(lines):
        game = [str(l.strip()) for l in line]  
        them = game[0]
        you = game[2]
        if (them == rock and you == paper2):
            results.append(win+paper_points)
        elif (them == paper and you == scissors2):
            results.append(win+scissors_points)
        elif (them == scissors and you == rock2):
            results.append(win+rock_points)
        elif (them == paper and you == paper2):
            results.append(draw+paper_points)
        elif (them == scissors and you == scissors2):
            results.append(draw+scissors_points)
        elif (them == rock and you == rock2):
            results.append(draw+rock_points)
        elif (them == scissors and you == paper2):
            results.append(loss+paper_points)
        elif (them == rock and you == scissors2):
            results.append(loss+scissors_points)
        elif (them == paper and you == rock2):
            results.append(loss+rock_points)

    return results

def part2(filename):
    results = []

    rock = "A"
    paper = "B"
    scissors = "C"

    tryLose = "X"
    tryDraw = "Y"
    tryWin = "Z"

    win = 6
    draw = 3
    loss = 0

    rock_points = 1
    paper_points = 2
    scissors_points = 3

    lines = read_file(filename)
    for count, line in enumerate(lines):
        game = [str(l.strip()) for l in line]  
        them = game[0]
        outcome = game[2]

        if (them == rock and outcome == tryWin):
            results.append(win+paper_points)
        elif (them == paper and outcome == tryWin):
            results.append(win+scissors_points)
        elif (them == scissors and outcome == tryWin):
            results.append(win+rock_points)
        elif (them == paper and outcome == tryDraw):
            results.append(draw+paper_points)
        elif (them == scissors and outcome == tryDraw):
            results.append(draw+scissors_points)
        elif (them == rock and outcome == tryDraw):
            results.append(draw+rock_points)
        elif (them == scissors and outcome == tryLose):
            results.append(loss+paper_points)
        elif (them == rock and outcome == tryLose):
            results.append(loss+scissors_points)
        elif (them == paper and outcome == tryLose):
            results.append(loss+rock_points)

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