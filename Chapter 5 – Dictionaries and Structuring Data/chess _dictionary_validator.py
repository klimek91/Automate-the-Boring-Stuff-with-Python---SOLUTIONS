dict = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
        '1h': 'bking','2h': 'bking','3h': 'bking','4h': 'bking','5h': 'bking','6h': 'bking',
        '7h': 'bking', '6h': 'bking',
        '1h': 'bking', '1b': 'bking', '1c': 'bking', '1h': 'bking', '8h': 'bking'}

def isValidChessBoard(dictionary):
    #kings
    if 'bking' not in dictionary.values() or 'wking' not in dictionary.values():
        return False
    #no more then 16 pieces each
    countb = 0
    countw = 0
    for value in dictionary.values():
        if value.startswith('b'):
            countb += 1
        if value.startswith('w'):
            countw += 1
    if countb >= 16 or countw >= 16:
        return False
    #only spots from 1a to 8h
    list = []
    for i in range(1, 9):
        for letter in ('abcdefgh'):
            list.append(str(i) + letter)
    for key in dictionary.keys():
        if key not in list:
            return False


isValidChessBoard(dict)
