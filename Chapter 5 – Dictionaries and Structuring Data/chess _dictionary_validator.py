def isValidChessBoard(dictionary):
    countb = 0
    countw = 0
    for value in dictionary.values():
        if value.startswith('b'):
            countb += 1
        if value.startswith('w'):
            countw += 1

    list = []
    for i in range(1, 9):
        for letter in ('abcdefgh'):
            list.append(str(i) + letter)

    #kings
    if 'bking' not in dictionary.values() or 'wking' not in dictionary.values():
        print("There is no white king or black king")
        return False
        #no more then 16 pieces each

    elif countb >= 16 or countw >= 16:
        print("There are to many white or\\and black pices")
        return False

    #only spots from 1a to 8h
    for key in dictionary.keys():
        if key not in list:
            print("You choose wrong spot")
            return False

    #correct names
    for value in dictionary.values():
        if not (value.startswith('b') or value.startswith('w')):
            print("Pices may be only black or white")
            return False
        elif not (value.endswith('pawn') or value.endswith('knight') or value.endswith('bishop')\
        or value.endswith('rook') or value.endswith('queen') or value.endswith('king')):
            print("Only possible pieces are pawn, knight, bishop, rook, queen and king")
            return False

    else:
        print("Everything is OK")
        return True
