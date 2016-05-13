#from othello import huong
import os
board = [-1,-1,-1,-1,-1,-1,-1,-1,-1, #8
     -1, 0, 0, 0, 0, 0, 0, 0, 0, #17
     -1, 0, 0, 0, 0, 0, 0, 0, 0, #26
     -1, 0, 0, 0, 0, 0, 0, 0, 0,
     -1, 0, 0, 0, 2, 1, 0, 0, 0,
     -1, 0, 0, 0, 1, 2, 0, 0, 0,
     -1, 0, 0, 0, 0, 0, 0, 0, 0,
     -1, 0, 0, 0, 0, 0, 0, 0, 0,
     -1, 0, 0, 0, 0, 0, 0, 0, 0,
     -1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
turn = 1
#print (huong(board, turn))
firstTurn = 1
secondTurn = 2
direction = [10, -10, 1, -1, 8, -8, 9, -9]

#cot = idx % 9 - 1
#hang = idx / 10 - 1
def isOnboard(idx):
    cot = idx % 9
    hang = idx / 10
    return 0 < cot < 9 and 0 < hang < 9


def isValidMove(board, move, turn):
    if turn == firstTurn:
        other = secondTurn
    else: other = firstTurn
    pos_cur = move
    tile2Flip = []
    for step in direction:
        temp = pos_cur + step
        isOver = True
        while board[temp] == other:
            temp = temp + step
            if not isOnboard(temp):
                isOver = False
                break
        if not isOver or board[temp] != turn:
           continue
        
        while temp - step != move:
            temp -= step
            tile2Flip.append(temp)
    return tile2Flip

def getMoveValid(board, turn):
    lstMove = []
    for i in range(10, 81):
        if isValidMove(board, i, turn):
            lstMove.append(i)
    return lstMove

def makeMove(board, turn, move):
    if not isOnboard(move):
        return
    flip = isValidMove(board, move, turn)
    if not flip:
        return False
    else:
        for i in flip:
            board[i] = turn
        board[move] = turn

def drawBoard(board):
    print (str(board[10:18])[1:-1])
    print (str(board[19:27])[1:-1])
    print (str(board[28:36])[1:-1])
    print (str(board[37:45])[1:-1])
    print (str(board[46:54])[1:-1])
    print (str(board[55:63])[1:-1])
    print (str(board[64:72])[1:-1])
    print (str(board[73:81])[1:-1])
   # print (str(board[10:90])[1:-1])

def getMoreBoard(board, turn):
    
    lst = [board]
    visited = []
    dem = 0
    bl = [board]
    wt = []
    while dem < 5000 and lst:
        #pt = bl.pop(0)
        #if turn == firstTurn:
        #    name = 'While'
        #else: name = 'Black'
        #print ("+-------------------")
        #drawBoard(pt)
   
        #print ("+++++++++++++++++++++++++++++++++++++++++++\nBoardtemp")
        #choos = getMoveValid(board, turn)
        #visited.append(pt)
        #for c in choos:
        #    boardtemp = [x for x in board]
        #    makeMove(boardtemp, turn, c)
        #    if turn == firstTurn:
        #        wt.append(boardtemp)
        #    else: bl.append(boardtemp)
        #    drawBoard(boardtemp)
        #    print ("+++++++++++++++++++++++++++++++++++++++++++\nBoardtemp")
        #    if boardtemp in visited:
        #        continue
        #    lst.append(boardtemp)
        #    dem = dem + 1
        #    f = open(name + str(dem) + '.txt', 'w')
        #    f.writelines(str(boardtemp)[1:-1])
        #    f.close()
        if turn == firstTurn:
            while bl:
                pt = bl.pop(0)
                choos = getMoveValid(board, turn)
                for c in choos:
                    boardtemp = [x for x in board]
                    makeMove(boardtemp, turn, c)
                    wt.append(boardtemp)
                    dem += 1
                    f = open('white' + str(dem) + '.txt', 'w')
                    f.writelines(str(boardtemp)[1:-1])
                    f.close()

                turn = secondTurn
        else:
            while wt:
                pt = wt.pop(0)
                choos = getMoveValid(board, turn)
                for c in choos:
                    boardtemp = [x for x in board]
                    makeMove(boardtemp, turn, c)
                    bl.append(boardtemp)
                    dem += 1
                    f = open('black' + str(dem) + '.txt', 'w')
                    f.writelines(str(boardtemp)[1:-1])
                    f.close()
                turn = firstTurn
def getPoint(board):
    bp = 0
    wp = 0
    for i in board:
        if i == 1:
            bp +=1
        elif i == 2:
            wp += 1
    return bp, wp

turn = firstTurn
import random as rd
ii = 0
##<<<<<<< HEAD
##dem = 0
####
####limitso = 100000
####while 1:
####    if ii > 1: break
####    ff, ss = getPoint(board)
####    if ff+ss > 58: break
####    if turn == firstTurn:
####        cho = getMoveValid(board, turn)
####        if cho:
####            ii=0
####            for c in cho:
####                bb = [x for x in board]
####                makeMove(bb, turn, c)
####                directory = "_second"
####                if not os.path.exists(directory):
####                    os.makedirs(directory)
####                path = os.path.join(directory, 'second' + str(dem) + '.txt')
####                f = open(path, 'w')
####                f.writelines(str(bb)[1:-1])
####                dem +=1
####                f.close()
####            rd.shuffle(cho)
####            makeMove(board, turn, cho[0])
####            turn = secondTurn
####        else:
####            ii += 1
####            turn = secondTurn
####    else:
####        cho = getMoveValid(board, turn)
####        if cho:
####            ii = 0
####            for c in cho:
####                bb = [x for x in board]
####                makeMove(bb, turn, c)
####                directory = "_first"
####                if not os.path.exists(directory):
####                    os.makedirs(directory)
####                path = os.path.join(directory, 'first' + str(dem) + '.txt')
####                f = open('first' + str(dem) + '.txt', 'w')
####                dem+=1
####                f.writelines(str(bb)[1:-1])
####                f.close()
####            rd.shuffle(cho)
####            makeMove(board, turn, cho[0])
####            turn = firstTurn
####        else:
####            ii += 1
####            turn = firstTurn
####print (len(board)+1)
##=======
##dem = 7000
##
##limitso = 100000
##while 1:
##    if ii > 1: break
##    ff, ss = getPoint(board)
##    if ff+ss > 58: break
##    if turn == firstTurn:
##        cho = getMoveValid(board, turn)
##        if cho:
##            ii=0
##            for c in cho:
##                bb = [x for x in board]
##                makeMove(bb, turn, c)
##                directory = "_second"
##                if not os.path.exists(directory):
##                    os.makedirs(directory)
##                path = os.path.join(directory, 'second' + str(dem) + '.txt')
##                f = open(path, 'w')
##                f.writelines(str(bb)[1:-1])
##                dem +=1
##                f.close()
##            rd.shuffle(cho)
##            makeMove(board, turn, cho[0])
##            turn = secondTurn
##        else:
##            ii += 1
##            turn = secondTurn
##    else:
##        cho = getMoveValid(board, turn)
##        if cho:
##            ii = 0
##            for c in cho:
##                bb = [x for x in board]
##                makeMove(bb, turn, c)
##                directory = "_first"
##                if not os.path.exists(directory):
##                    os.makedirs(directory)
##                path = os.path.join(directory, 'first' + str(dem) + '.txt')
##                f = open('first' + str(dem) + '.txt', 'w')
##                dem+=1
##                f.writelines(str(bb)[1:-1])
##                f.close()
##            rd.shuffle(cho)
##            makeMove(board, turn, cho[0])
##            turn = firstTurn
##        else:
##            ii += 1
##            turn = firstTurn
##print (len(board)+1)
##>>>>>>> c09b95925119ce34c1a2f0d4d1712ef6919364f8
def createInput(vBoard):
    pass
