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
    for result in pt2results:
        print(result)   
    #print (sum(pt2results)) 
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    results = []

    lines = read_file(filename)
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0

    y_line = 10 if filename.startswith("example") else 2000000
    print(f"Evaluating for y_line: {y_line}")
    coords = []
    for count, line in enumerate(lines):
        #parse the data
        splitline = line.split(" ")
        sensor_x = int(''.join( l for l in splitline[2] if l not in 'xy=,:'))
        sensor_y = int(''.join( l for l in splitline[3] if l not in 'xy=,:'))
        beacon_x = int(''.join( l for l in splitline[8] if l not in 'xy=,:'))
        beacon_y = int(''.join( l for l in splitline[9] if l not in 'xy=,:'))
        taxi_distance = get_taxi_distance(sensor_x, sensor_y, beacon_x, beacon_y)
        coords.append((sensor_x, sensor_y, beacon_x, beacon_y, taxi_distance))

        #work out the bounds
        max_x = max(max_x, sensor_x, beacon_x)
        max_y = max(max_y, sensor_y, beacon_y)
        min_x = min(min_x, sensor_x, beacon_x)
        min_y = min(min_y, sensor_y, beacon_y)

       # print (f"{sensor_x}, {sensor_y} : {beacon_x}, {beacon_y}")
        
    print (f"Original: {min_x}, {min_y} to {max_x}, {max_y}")

    normalised_coords = []
    #NORMALISE everything to only be positive numbers!    
    for _, line in enumerate(coords):  
        (s_x, s_y, b_x, b_y, taxi_distance) = line  
        if min_x < 0: 
            s_x = s_x - min_x
            b_x = b_x - min_x
        if min_y < 0:
            s_y = s_y - min_y
            b_y = b_y - min_y
        normalised_coords.append((s_x, s_y, b_x, b_y, taxi_distance))
    if min_x < 0: 
        max_x = max_x - min_x
        min_x = min_x - min_x
    if min_y < 0:
        y_line = y_line - min_y
        max_y = max_y - min_y
        min_y = min_y - min_y

    #From now we only use normalised_coords!
    print (f"Normalised: {min_x}, {min_y} to {max_x}, {max_y}")

    # we only need to worry about the y_line
    grid = [0] * (max_x +1)

    for count, line in enumerate(normalised_coords):
        (s_x, s_y, b_x, b_y, taxi_distance) = line
        #mark the special items
        if s_y == y_line:
            grid[s_x] = 110
        if b_y == y_line:
            grid[b_x] = 100
        
        #work out which part of the line is "covered" by this particular sensor
        y_dist = abs(s_y - y_line)
        x_dist = taxi_distance - y_dist

        print(f"x_dist={x_dist}, y_dist={y_dist}")
        if x_dist >= 0:
            covered_min = s_x - (x_dist) #(x_dist//2)
            covered_max = s_x + (x_dist) #(x_dist//2)
           # print(f"For sensor {s_x},{s_y} to reach {b_x}, {b_y} - it has an x-distance of {x_dist} and so covers {covered_min} to {covered_max}")
            for i in range(covered_min, covered_max +1):
                if i >= len(grid):
                    break
                if grid[i] == 0:
                    grid[i] = 1

    #4096105
    
    #print(grid)

    # for x_coord in range(len(grid)):
    #     for count, line in enumerate(normalised_coords):
    #         (s_x, s_y, b_x, b_y, taxi_distance) = line
    #         if s_y == y_line:
    #             grid[s_x] = 5
    #         if b_y == y_line:
    #             grid[b_x] = 10
            
    #         dist = get_taxi_distance(s_x, s_y, x_coord, y_line) 
    #         if dist <= taxi_distance and grid[x_coord] == 0:
    #             grid[x_coord] = 1
    #             break

    #     continue
    #print(grid)    
    #print (np.count_nonzero(grid[:, y_line]))

    result = len([g for g in grid if g == 1])
    print (f"count: {result}")

    #display_grid = np.array(grid).reshape(1, max_x +1)
    #plt.imshow(display_grid, extent=[0, max_x, 0, 1], cmap="RdGy")
    #plt.show()
    return result

def get_taxi_distance(s_x, s_y, b_x, b_y):
    dist = abs(s_x - b_x) + abs(s_y - b_y)
    #print(f"{dist} between {s_x},{s_y} and {b_x},{b_y}")
    return dist

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