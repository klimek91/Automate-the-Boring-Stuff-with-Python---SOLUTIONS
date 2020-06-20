import random, time, copy

width = 60
height = 20

nextCells = []
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0,1) == 0:
            column.append("#")
        else:
            column.append(' ')
    nextCells.append(column)

#test
for x in nextCells:
    print(x)
