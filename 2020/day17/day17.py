#day 17
from collections import defaultdict
import copy


def getNumberOfNeighboursPart1(grid, coordinate):
    neighIndices = [-1, 0, 1]
    counter = 0
    for x in neighIndices:
        for y in neighIndices:
            for z in neighIndices:
                # don't consider my position as neighbour -> exclude (0,0,0)
                if (not x == y == z == 0 and grid[coordinate[0] + x, 
                    coordinate[1] + y, coordinate[2] + z] == '#'):
                    counter +=1
    return counter


def computePart1(lines, cycles):
    # 3D grid
    grid = defaultdict(lambda: ".")

    for row in range(len(lines)):
        for column in range(len(lines[0])):
            # x, y, z = 0 for first input
            grid[row, column, 0] = lines[row][column]
    
    for _ in range(cycles):
        new_grid = defaultdict(lambda: ".")

        # need to get the min and max interval of x,y,z,k coorinates
        x_min = min(grid.keys(), key=lambda x : x[0])[0] - 1 # -1 to check one layer below
        x_max = max(grid.keys(), key=lambda x : x[0])[0] + 1 # +1 to check one layer higher
        y_min = min(grid.keys(), key=lambda x : x[1])[1] - 1
        y_max = max(grid.keys(), key=lambda x : x[1])[1] + 1
        z_min = min(grid.keys(), key=lambda x : x[2])[2] - 1
        z_max = max(grid.keys(), key=lambda x : x[2])[2] + 1

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    numberOfNeighbours = getNumberOfNeighboursPart1(grid, (x, y, z))

                    if grid[x, y, z] == "#":
                        if numberOfNeighbours in [2,3]:
                            new_grid[x, y, z] = "#"

                    else:
                        if numberOfNeighbours in [3]:
                            new_grid[x, y, z] = "#"

        grid = copy.deepcopy(new_grid)

    cubes = sum(value == '#' for value in grid.values())
    return cubes


def getNumberOfNeighboursPart2(grid, coordinate):
    neighIndices = [-1, 0, 1]
    counter = 0
    for x in neighIndices:
        for y in neighIndices:
            for z in neighIndices:
                for k in neighIndices:
                    # don't consider my position as neighbour -> exclude (0,0,0,0)
                    if (not x == y == z == k == 0 and 
                        grid[coordinate[0] + x, coordinate[1] + y, 
                        coordinate[2] + z, coordinate[3] + k] == '#'):
                        counter +=1
    return counter


def computePart2(lines, cycles):
    # 4D grid
    grid = defaultdict(lambda: ".")

    for row in range(len(lines)):
        for column in range(len(lines[0])):
            # x, y, z, k = 0 for first input
            grid[row, column, 0, 0] = lines[row][column]
    
    for _ in range(cycles):
        new_grid = defaultdict(lambda: ".")

        # need to get the min and max interval of x,y,z,k coorinates
        x_min = min(grid.keys(), key=lambda x : x[0])[0] - 1 # -1 to check one layer below
        x_max = max(grid.keys(), key=lambda x : x[0])[0] + 1 # +1 to check one layer higher
        y_min = min(grid.keys(), key=lambda x : x[1])[1] - 1
        y_max = max(grid.keys(), key=lambda x : x[1])[1] + 1
        z_min = min(grid.keys(), key=lambda x : x[2])[2] - 1
        z_max = max(grid.keys(), key=lambda x : x[2])[2] + 1
        k_min = min(grid.keys(), key=lambda x : x[3])[3] - 1
        k_max = max(grid.keys(), key=lambda x : x[3])[3] + 1

        for x in range(x_min, x_max + 1):
            for y in range(y_min, y_max + 1):
                for z in range(z_min, z_max + 1):
                    for k in range(k_min, k_max + 1):
                        numberOfNeighbours = getNumberOfNeighboursPart2(grid, (x, y, z, k))

                        if grid[x, y, z, k] == "#":
                            if numberOfNeighbours in [2,3]:
                                new_grid[x, y, z, k] = "#"

                        else:
                            if numberOfNeighbours in [3]:
                                new_grid[x, y, z, k] = "#"

        grid = copy.deepcopy(new_grid)

    cubes = sum(value == '#' for value in grid.values())
    return cubes


if __name__ == "__main__":
    with open("input", 'r') as input:
        lines = input.read().splitlines()
        # print(lines)
    
    print("Part1: " + str(computePart1(lines, 6)))
    print("Part2: " + str(computePart2(lines, 6)))