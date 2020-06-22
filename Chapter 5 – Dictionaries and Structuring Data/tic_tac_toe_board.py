board = {'topLeft' : ' ', 'topMid' : ' ', 'topRight': ' ',
         'midLeft' : ' ', 'midMid' : ' ', 'midRight': ' ',
         'bottomLeft' : ' ', 'bottomMid': ' ', 'bottomRight': ' '}


def printBoard(board):
    print(board['topLeft'] + '|' + board['topMid'] + '|' + board['topRight'])
    print('-+-+-')
    print(board['midLeft'] + '|' + board['midMid'] + '|' + board['midRight'])
    print('-+-+-')
    print(board['bottomLeft'] + '|' + board['bottomMid'] + '|' + board['bottomRight'])

printBoard(board)