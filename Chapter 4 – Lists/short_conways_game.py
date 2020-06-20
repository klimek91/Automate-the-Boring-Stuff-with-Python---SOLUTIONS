import random, time, copy

width = 60
height = 20
step = 0
board = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append("#")
        else:
            column.append(' ')
    board.append(column)


currentBoard = copy.deepcopy(board)

def printBoard(board):
    for x in range(width):
        for y in range(height):
            print(board[x][y], end='')
        print()


for x in range(width):
    for y in range(height):
        leftCoord = (x-1) % width
        rightCoord = (x+1) % width
        aboveCoord = (y-1) % height
        belowCoord = (y+1) % height

        numNeighbors = 0
        if currentBoard[leftCoord][aboveCoord] == '#':
            numNeighbors +=1
        if currentBoard[x][aboveCoord] == '#':
            numNeighbors +=1
        if currentBoard[rightCoord][aboveCoord] == '#':
            numNeighbors += 1
        if currentBoard[rightCoord][y] == '#':
            numNeighbors += 1
        if currentBoard[rightCoord][belowCoord] == '#':
            numNeighbors += 1
        if currentBoard[x][belowCoord] == '#':
            numNeighbors += 1
        if currentBoard[leftCoord][belowCoord] == '#':
            numNeighbors += 1
        if currentBoard[leftCoord][y] == '#':
            numNeighbors += 1
