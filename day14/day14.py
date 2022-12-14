import sys
import time
import numpy as np
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
    print (pt2results)  
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):   
    size = 1000

    grid = np.zeros((size, size))

    lines = read_file(filename)
    
    for _, line in enumerate(lines):
        new_line = line.split("->")
        for i, l in enumerate(new_line[:-1]):            
            from_xy = l.split(",")
            from_x = int(from_xy[0])
            from_y = int(from_xy[1])

            to_xy = new_line[i+1].split(",")
            to_x = int(to_xy[0])
            to_y = int(to_xy[1])

            #print(f"{from_x},{from_y} to {to_x},{to_y}")
            if from_x == to_x: 
                if from_y < to_y:
                    for y in range(from_y, to_y + 1):
                        grid[from_x, y] = 10
                else:
                    for y in range(to_y, from_y + 1):
                        grid[from_x, y] = 10
            else:
                if from_x < to_x:
                    for x in range(from_x, to_x + 1):
                        grid[x, from_y] = 10
                else:
                    for x in range(to_x, from_x + 1):
                        grid[x, from_y] = 10
        continue
    
    units_of_sand = 0
    abyss = False
    #Simulate SAND
    for i in range(10000): #while we still need to simulate sand
        sand_x = 500
        sand_y = 0
        while (True):
            if sand_y >= 200:
                abyss = True
                break
            if grid[sand_x, sand_y +1] == 0: #space to fall down directly
                sand_y = sand_y + 1
                continue
            elif grid[sand_x - 1, sand_y + 1] == 0: #space to fall down and to the left
                sand_x = sand_x - 1
                sand_y = sand_y + 1
                continue
            elif grid[sand_x + 1, sand_y + 1] == 0: #space to fall down and to the right
                sand_x = sand_x + 1
                sand_y = sand_y + 1
                continue
            else: #sand has come to a stop
                grid[sand_x, sand_y] = 5
                units_of_sand = units_of_sand + 1
                break
        if abyss:
            break

    grid[500,0] = 1
    display_grid = np.swapaxes(grid,0,1)
    plt.imshow(display_grid, extent=[0, size, 0, size], cmap="RdGy")
    #plt.show()

    return units_of_sand

def part2(filename):
    size = 1000

    grid = np.zeros((size, size))

    lines = read_file(filename)
    highest_y = 0
    for _, line in enumerate(lines):
        new_line = line.split("->")
        for i, l in enumerate(new_line[:-1]):            
            from_xy = l.split(",")
            from_x = int(from_xy[0])
            from_y = int(from_xy[1])

            to_xy = new_line[i+1].split(",")
            to_x = int(to_xy[0])
            to_y = int(to_xy[1])

            if to_y > highest_y:
                highest_y = to_y
            if from_y > highest_y:
                highest_y = from_y

            #print(f"{from_x},{from_y} to {to_x},{to_y}")
            if from_x == to_x: 
                if from_y < to_y:
                    for y in range(from_y, to_y + 1):
                        grid[from_x, y] = 10
                else:
                    for y in range(to_y, from_y + 1):
                        grid[from_x, y] = 10
            else:
                if from_x < to_x:
                    for x in range(from_x, to_x + 1):
                        grid[x, from_y] = 10
                else:
                    for x in range(to_x, from_x + 1):
                        grid[x, from_y] = 10
    for x in range(0, size):
        grid[x, highest_y+2] = 10
    
    units_of_sand = 0
    stop = False
    #Simulate SAND
    for i in range(100000): #while we still need to simulate sand 
        sand_x = 500
        sand_y = 0
        while (True):
            if sand_y >= 200:
                stop = True
                break
            if grid[sand_x, sand_y +1] == 0: #space to fall down directly
                sand_y = sand_y + 1
                continue
            elif grid[sand_x - 1, sand_y + 1] == 0: #space to fall down and to the left
                sand_x = sand_x - 1
                sand_y = sand_y + 1
                continue
            elif grid[sand_x + 1, sand_y + 1] == 0: #space to fall down and to the right
                sand_x = sand_x + 1
                sand_y = sand_y + 1
                continue
            else: #sand has come to a stop
                grid[sand_x, sand_y] = 5
                units_of_sand = units_of_sand + 1
                if sand_x == 500  and sand_y == 0:
                    stop = True
                break
        if stop:
            break

    grid[500,0] = 1
    display_grid = np.swapaxes(grid,0,1)
    plt.imshow(display_grid, extent=[0, size, 0, size], cmap="RdGy")
    #plt.show()

    return units_of_sand

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)