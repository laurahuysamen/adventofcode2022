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
    print (sum(pt1results))

    print ("PART 2 RESULTS:")
    for i in range(6):
        print("".join(pt2results[i*40:i*40+40]))
    
    print(f"Part 1 Time: {str(middle-start)}")
    print(f"Part 2 Time: {str(end-middle)}")
    print(f"Total Time: {str(end-start)}")
    
    
def part1(filename):     
    X_values = [1]
    signal_strength = [1]
    X  = 1
    cycle_number = 1
    
    lines = read_file(filename)
    for count, line in enumerate(lines):
        splitline = line.split(" ")
        if splitline[0] == "noop":

            X_values.append(X)
            signal_strength.append(X * cycle_number)
            cycle_number = cycle_number + 1

        elif splitline[0] == "addx":

            X_values.append(X)
            signal_strength.append(X*cycle_number)
            cycle_number = cycle_number + 1

            X_values.append(X)
            signal_strength.append(X*cycle_number)
            X = X + int(splitline[1])
            cycle_number = cycle_number + 1

    X_values.append(X)
    signal_strength.append(X*cycle_number)

    return [signal_strength[20],signal_strength[60],signal_strength[100],signal_strength[140], signal_strength[180] ,signal_strength[220]]

def part2(filename):
    X_values = [1]
    signal_strength = [1]
    X  = 1
    cycle_number = 1
    screen = []

    lines = read_file(filename)
    for count, line in enumerate(lines):
        splitline = line.split(" ")
        if splitline[0] == "noop":

            X_values.append(X)
            signal_strength.append(X * cycle_number)
            #draw to screen
            screen_position = (cycle_number - 1) % 40
            pixel = "#" if X == screen_position or X-1 == screen_position or X + 1 == screen_position else "."
            screen.append(pixel)
            cycle_number = cycle_number + 1

        elif splitline[0] == "addx":

            X_values.append(X)
            signal_strength.append(X*cycle_number)
            #draw to screen
            screen_position = (cycle_number - 1) % 40
            pixel = "#" if X == screen_position or X - 1 == screen_position or X + 1 == screen_position else "."
            screen.append(pixel)
            cycle_number = cycle_number + 1

            X_values.append(X)
            signal_strength.append(X*cycle_number)
            #draw to screen
            screen_position = (cycle_number - 1) % 40
            pixel = "#" if X == screen_position or X - 1 == screen_position or X + 1 == screen_position else "."
            screen.append(pixel)
            X = X + int(splitline[1])
            cycle_number = cycle_number + 1

    X_values.append(X)
    signal_strength.append(X*cycle_number)

    return screen

if __name__ == "__main__":
    filename = "input.txt"
    if len(sys.argv) > 1: 
        if sys.argv[1] == "0":
            filename = "example_input.txt"
        else:
            filename = f"example_input{sys.argv[1]}.txt"
    #filename = 
    main(filename)