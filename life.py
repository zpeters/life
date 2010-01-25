#!/usr/bin/env python
import sys
import random
import time
import os

LIVECHAR = '-'
OLDLIVECHAR = '='
DEADCHAR = ' '
LIFECHANCE = 28
UPDATESPEED = 0.06
GRIDWIDTH = 5
GRIDHEIGHT = 5

def getTerminalSize():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return None
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (env['LINES'], env['COLUMNS'])
        except:
            cr = (25, 80)
    return int(cr[1]), int(cr[0])

def initBoard():
    # set dynamic grid size, if possible
    global GRIDWIDTH
    global GRIDHEIGHT

    (width, height) = getTerminalSize()

    GRIDWIDTH = width - 2
    GRIDHEIGHT = height - 3

    board = []
    for i in range(GRIDHEIGHT):
        row = []
        for j in range(GRIDWIDTH):
            lifeSpark = random.randrange(1,100)
            if lifeSpark < LIFECHANCE:
                state = 1
            else:
                state = 0
            row.append(state)
        board.append(row)
    return board

def printBoard(board):
    # print top of board
    sys.stdout.write("+")
    for i in range(GRIDWIDTH):
        sys.stdout.write("-")
    sys.stdout.write("+\n")

    for row in range(GRIDHEIGHT):
        sys.stdout.write("|")
        for cell in range(GRIDWIDTH):
            if board[row][cell] == 1:
                sys.stdout.write(LIVECHAR)
            elif board[row][cell] > 1:
                sys.stdout.write(OLDLIVECHAR)
            else:
                sys.stdout.write(DEADCHAR)
        sys.stdout.write("|\n")

    # print bottom of board
    sys.stdout.write("+")
    for i in range(GRIDWIDTH):
        sys.stdout.write("-")
    sys.stdout.write("+\n")

def updateBoard(board):
    newBoard = []
    for row in range(GRIDHEIGHT):
        rowArray = []
        for col in range(GRIDWIDTH):
            state = board[row][col]
            newState = testLife(state, getNeighbors(board, row, col))
            if state == 1 and newState == 1:
                newState = 2
            rowArray.append(newState)
        newBoard.append(rowArray)
    return newBoard

def testLife(state, neighborsValues):
    newState = 0
    if (state == 1 or state == 2) and neighborsValues < 2:
        newState = 0

    if (state == 1 or state == 2) and neighborsValues > 3:
        newState = 0

    if ((state == 1 or state ==2) and neighborsValues == 2) or ((state == 1 or state==2) and neighborsValues == 3):
        newState = 1

    if state == 0 and neighborsValues == 3:
        newState = 1

    return newState

def getNeighbors(board, row, col):
    # 1 2 3
    # 4 * 5
    # 6 7 8
    try:
        neighbor1 = board[row-1][col-1]
    except IndexError:
        neighbor1 = 0

    try:
        neighbor2 = board[row-1][col]
    except IndexError:
        neighbor2 = 0

    try:
        neighbor3 = board[row-1][col+1]
    except IndexError:
        neighbor3 = 0

    try:
        neighbor4 = board[row][col-1]
    except IndexError:
        neighbor4 = 0

    try:
        neighbor5 = board[row][col+1]
    except IndexError:
        neighbor5 = 0

    try:
        neighbor6 = board[row+1][col-1]
    except IndexError:
        neighbor6 = 0

    try:
        neighbor7 = board[row+1][col]
    except IndexError:
        neighbor7 = 0

    try:
        neighbor8 = board[row+1][col+1]
    except IndexError:
        neighbor8 = 0

    neighbors = neighbor1 + neighbor2 + neighbor3 + neighbor4 + neighbor5 + neighbor6 + neighbor7 + neighbor8
    return int(neighbors)

def boardAlive(board):
    sum = 0
    for line in board:
        for item in line:
            sum = sum + item
    return sum
            
def main():
    board = initBoard()
    while 1:
        printBoard(board)
        board = updateBoard(board)
        if not boardAlive(board):
            board = initBoard()
        time.sleep(UPDATESPEED)
    
if __name__ == "__main__":
    main()
