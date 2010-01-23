#!/usr/bin/env python
import sys
import random
import time

LIVECHAR = "+"
DEADCHAR = " "
LIFECHANCE = 9
UPDATESPEED = 0.1
GRIDWIDTH = 39 
GRIDHEIGHT = 39 

def gridPrinter(grid):
    height = len(grid)
    width = len(grid[0])
    print "+" + "-"*height + "+"
    for line in grid:
        sys.stdout.write("|")
        for cell in line:
            if cell == 0:
                sys.stdout.write(DEADCHAR)
            elif cell == 1:
                sys.stdout.write(LIVECHAR)
        sys.stdout.write("|\n")
    print "+" + "-"*height + "+"
    
def initBoard(width, height):
    grid = []
    for x in range(0,width):
        line = []
        for y in range(0,height):
            spawn = random.random() * 100
            if spawn <= LIFECHANCE:
                line.append(1)
            else: 
                line.append(0)
        grid.append(line)
    return grid

def checkCell(grid, x, y):
    height = len(grid)
    width = len(grid[0])
    state = grid[x][y]

    if (x > 0 and x < width-1) and (y > 0 and y < height-1):
        topNeighbors = grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1]
        sameNeighbors = grid[x][y-1] + grid[x][y+1]
        bottomNeighbors = grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1]
        neighbors = topNeighbors + sameNeighbors + bottomNeighbors

        if state == 1 and neighbors < 2:
            newState = 0
            return newState

        if state == 1 and neighbors > 3:
            newState = 0
            return newState

        if state == 1 and neighbors == 2:
            newState = 1
            return newState

        if state == 1 and neighbors == 3:
            newState = 1
            return newState

        if state == 0 and neighbors == 3:
            newState = 1
            return newState

    return state

def updateGrid(grid):
    height = len(grid)
    width = len(grid[0])
    newGrid = []
    
    for x in range(0,height):
        newLine = []
        for y in range(0, width):
            newLine.append(checkCell(grid, x, y))
        newGrid.append(newLine)

    return newGrid
    
def main():
    while 1:
        grid = initBoard(GRIDWIDTH,GRIDHEIGHT)
        grid = updateGrid(grid)
        gridPrinter(grid)
        time.sleep(UPDATESPEED)

if __name__ == "__main__":
    main()
