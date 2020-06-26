tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):
    #table size (for rjust)
    tableWidth = [0,0,0]
    for word in range(len(table[0])):
        for list in range(len(table)):
            if tableWidth[list] < len(table[list][word]):
                tableWidth[list] = len(table[list][word])
    #table size 1 more then max len word ea table
    for i in range(len(tableWidth)):
        tableWidth[i] +=1

    #table print
    for word in range(len(table[0])):
        for list in range(len(table)):
            print(table[list][word].rjust(tableWidth[list]), end='')
        print()

printTable(tableData)