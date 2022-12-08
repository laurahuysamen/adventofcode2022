import sys
import time
import numpy as np


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
    print (len(pt1results))

    print ("PART 2 RESULTS:")
    print (pt2results)
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename): 
    lines = read_file(filename)

    forest = np.array([[int(l) for l in list(line)] for line in lines])
    num_rows, num_cols = forest.shape
    
    visibles = []
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if x == 0 or y == 0 or x == num_rows - 1 or y == num_cols - 1:
                visibles.append((x, y))
            else:
                current_tree = forest[x, y]

                #check x
                maxHeight = 0
                for i in range(0, x):
                    if forest[i, y] > maxHeight:
                        maxHeight = forest[i, y]
                if maxHeight < current_tree:
                    visibles.append((x, y))
                    continue

                maxHeight = 0
                for i in range(x + 1, num_rows):
                    if forest[i, y] > maxHeight:
                        maxHeight = forest[i, y]
                if maxHeight < current_tree:
                    visibles.append((x, y))
                    continue

                #check y
                maxHeight = 0
                for j in range(0, y):
                    if forest[x, j] > maxHeight:
                        maxHeight = forest[x, j]
                if maxHeight < current_tree:
                    visibles.append((x, y))
                    continue

                maxHeight = 0
                for j in range(y + 1, num_cols):
                    if forest[x, j] > maxHeight:
                        maxHeight = forest[x, j]
                if maxHeight < current_tree:
                    visibles.append((x, y))
                    continue

    return visibles

def part2(filename):
    lines = read_file(filename)

    forest = np.array([[int(l) for l in list(line)] for line in lines])
    scenic_scores = np.empty(forest.shape, int)

    num_rows, num_cols = forest.shape
    for x in range(0, num_rows):
        for y in range(0, num_cols):
            if x == 0 or y == 0 or x == num_rows - 1 or y == num_cols - 1:
                scenic_scores[x, y] = 0
            else:
                x_score1=0
                x_score2=0
                y_score1=0
                y_score2=0
                current_tree = forest[x, y]

                #check x
                numtrees = 1
                for i in reversed(range(0,x)): #work away from the tree
                    if forest[i, y] >= current_tree or ((i == 0 or i == num_rows - 1)):
                        break
                    else:
                        numtrees = numtrees + 1
                x_score1 = numtrees

                numtrees = 1
                for i in range(x + 1, num_rows):
                    if forest[i, y] >= current_tree or ((i == 0 or i == num_rows - 1)):
                        break
                    else:
                        numtrees = numtrees + 1
                x_score2 = numtrees 

                numtrees = 1
                for j in reversed(range(0, y)): #work away from the tree
                    if forest[x, j] >= current_tree or ((j == 0 or j == num_cols - 1)):
                        break
                    else:
                        numtrees = numtrees + 1                        
                y_score1 = numtrees 
                
                numtrees = 1
                for j in range(y + 1, num_cols):
                    if forest[x, j] >= current_tree or (j == 0 or j == num_cols - 1):
                        break
                    else:
                        numtrees = numtrees + 1
                y_score2 = numtrees 
                
                scenic_scores[x, y] = (x_score1 * x_score2 * y_score1 * y_score2)

    return scenic_scores.max()

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)