import random, time, copy, sys

width = 10
height = 10

board = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append("#")
        else:
            column.append(' ')
    board.append(column)



step = 0
while True:
    print("Step no.{}".format(step+1))
    currentBoard = copy.deepcopy(board)
    step +=1

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
                numNeighbors += 1
            if currentBoard[x][aboveCoord] == '#':
                numNeighbors += 1
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

            if currentBoard[x][y] == '#' and (numNeighbors ==2 or numNeighbors ==3):
                board[x][y] = '#'
            elif currentBoard[x][y] == ' ' and numNeighbors == 3:
                board[x][y] = '#'
            else:
                board[x][y] = ' '
    cellsLiving = 0
    for x in range(width):
        for y in range (height):
            if board[x][y] == '#':
                cellsLiving +=1

    if cellsLiving == 0:
        print("All cells died in {} steps".format(step))
        sys.exit()

    print('\n\n')
    time.sleep(0)
