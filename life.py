#!/usr/bin/env python
import sys
import random
import time

LIVECHAR = "+"
DEADCHAR = " "
LIFECHANCE = 10
UPDATESPEED = 0.1
GRIDWIDTH = 20
GRIDHEIGHT = 10

def gridPrinter(grid):
    print "+" + "-"*GRIDHEIGHT + "+"
    for line in grid:
        sys.stdout.write("|")
        for cell in line:
            if cell == 0:
                sys.stdout.write(DEADCHAR)
            elif cell == 1:
                sys.stdout.write(LIVECHAR)
        sys.stdout.write("|\n")
    print "+" + "-"*GRIDHEIGHT + "+"
    
def initBoard():
    grid = []
    for x in range(0,GRIDWIDTH):
        line = []
        for y in range(0,GRIDHEIGHT):
            spawn = random.random() * 100
            if spawn <= LIFECHANCE:
                line.append(1)
            else: 
                line.append(0)
        grid.append(line)
    return grid

def checkCell(grid, x, y):
    print "Grid is %sx%s" % (GRIDWIDTH, GRIDHEIGHT)
    print "Checking cell [%s][%s] = %s" % (x,y, grid[x][y])
    state = grid[x][y]

    print "Checking bounds..."
    if (x > 0 and x < GRIDWIDTH-1) and (y > 0 and y < GRIDWIDTH -1):
        print "INside if statemetn"
        topNeighbors = grid[x-1][y-1] + grid[x-1][y] + grid[x-1][y+1]
        sameNeighbors = grid[x][y-1] + grid[x][y+1]
        bottomNeighbors = grid[x+1][y-1] + grid[x+1][y] + grid[x+1][y+1]
        neighbors = topNeighbors + sameNeighbors + bottomNeighbors

        if state == 1 and neighbors < 2:
            print "Not enough neighbors, dying"
            newState = 0
            return newState

        if state == 1 and neighbors > 3:
            print "Too many neighbors, dying"
            newState = 0
            return newState

        if state == 1 and neighbors == 2:
            print "Maintaining equilibruim"
            newState = 1
            return newState

        if state == 1 and neighbors == 3:
            print "Maintaining equilibruim"
            newState = 1
            return newState

        if state == 0 and neighbors == 3:
            print "Neighbors just spawned me"
            newState = 1
            return newState

    return state

def updateGrid(grid):
    newGrid = []
    
    for x in range(0,GRIDHEIGHT):
        newLine = []
        for y in range(0, GRIDWIDTH):
            newLine.append(checkCell(grid, x, y))
        newGrid.append(newLine)

    return newGrid
    
def main():
   # while 1:
   grid = initBoard()
   grid = updateGrid(grid)
   gridPrinter(grid)
    # time.sleep(UPDATESPEED)

if __name__ == "__main__":
    main()
