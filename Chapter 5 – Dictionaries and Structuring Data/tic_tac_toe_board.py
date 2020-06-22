import random

board = {'topLeft' : ' ', 'topMid' : ' ', 'topRight': ' ',
         'midLeft' : ' ', 'midMid' : ' ', 'midRight': ' ',
         'bottomLeft' : ' ', 'bottomMid': ' ', 'bottomRight': ' '}


def printBoard(board):
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'])
    print('-+-+-')
    print(board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'])
    print('-+-+-')
    print(board['bottomLeft'] + '|' + board['bottomMid'] + '|' + board['bottomRight'])

turn = random.choice(['X', 'O'])

print("Player '{}' is starting...".format(turn))
print("""Possible spots:
topLeft, topMid, topRight
midLeft, midMid, midRight
bottomLeft, bottomMid, bottomRight""")

for i in range(9):
    printBoard(board)
    print("Turn no. {} player {}".format(i+1, turn))
    spot = input("Choose Your spot: ")
    board[spot] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

