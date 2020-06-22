dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
        '1h': 'bking','2h': 'bking','3h': 'bking','4h': 'bking','5h': 'bking','6h': 'bking',
        '1f': 'bking','1a': 'bking', '1d': 'bking', '1h': 'bking', '7h': 'bking', '10h': 'bking',
        '1h': 'bking', '1b': 'bking', '1c': 'bking', '1h': 'bking', '8h': 'bking', '9h': 'bking'}


print(dict.values())
print(dict.keys())
print(len(dict.values()))


def isValidChessBoard(dictionary):
    if 'bking' not in dictionary.values() or 'wking' not in dictionary.values():
        print('false')
        return False
    countb = 0
    countw = 0
    for value in dictionary.values():
        if value.startswith('b'):
            countb += 1
        if value.startswith('w'):
            countw += 1
    if countb >= 16 or countw >= 16:
        print('false')


isValidChessBoard(dict)