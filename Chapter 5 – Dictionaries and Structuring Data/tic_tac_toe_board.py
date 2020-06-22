import random, sys

board = {'topLeft' : ' ', 'topMid' : ' ', 'topRight': ' ',
         'midLeft' : ' ', 'midMid' : ' ', 'midRight': ' ',
         'bottomLeft' : ' ', 'bottomMid': ' ', 'bottomRight': ' '}


def printBoard(board):
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'])
    print('-+-+-')
    print(board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'])
    print('-+-+-')
    print(board['bottomLeft'] + '|' + board['bottomMid'] + '|' + board['bottomRight'])

def winCond(board, player):
    if (board['topLeft'] == board['topMid'] == board['topRight'] == 'O')\
    or(board['midLeft'] == board['midMid'] == board['midRight'] == 'O')\
    or (board['bottomLeft'] == board['bottomMid'] == board['bottomRight'] == 'O')\
    or (board['topLeft'] == board['midLeft'] == board['bottomLeft'] == 'O') \
    or (board['topMid'] == board['midMid'] == board['bottomMid'] == 'O') \
    or (board['topRight'] == board['midRight'] == board['bottomRight'] == 'O') \
    or (board['topLeft'] == board['midMid'] == board['bottomRight'] == 'O') \
    or (board['bottomLeft'] == board['midMid'] == board['topRight'] == 'O')\
    or (board['topLeft'] == board['topMid'] == board['topRight'] == 'X') \
    or (board['midLeft'] == board['midMid'] == board['midRight'] == 'X') \
    or (board['bottomLeft'] == board['bottomMid'] == board['bottomRight'] == 'X') \
    or (board['topLeft'] == board['midLeft'] == board['bottomLeft'] == 'X') \
    or (board['topMid'] == board['midMid'] == board['bottomMid'] == 'X') \
    or (board['topRight'] == board['midRight'] == board['bottomRight'] == 'X') \
    or (board['topLeft'] == board['midMid'] == board['bottomRight'] == 'X') \
    or (board['bottomLeft'] == board['midMid'] == board['topRight'] == 'X'):
        print("Player '{}' wins".format(player))
        sys.exit()

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
    while spot not in board.keys():
        print("You choose wrong spot, please try again")
        spot = input()
    while board[spot] != ' ':
        print("This spot is already taken, pleasy try again")
        spot = input()
    if spot in board.keys():
        board[spot] = turn
        winCond(board,turn)
        if turn == "X":
            turn = "O"
        else:
            turn = "X"


