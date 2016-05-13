import random
from othello import huong
from NeuralClass import getPoint as ggpp, getMoveValid, makeMove as mmkk

scoreBoard = [
              [120, -20,  20,   10,   10,  20, -20, 120],
              [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
              [20,  -5,  15,   5,   5,  15,  -5,  20],
              [10,  -5,   5,   3,   3,   5,  -5,   10],
              [10,  -5,   5,   3,   3,   5,  -5,   10],
              [20,  -5,  15,   5,   5,  15,  -5,  20],
              [-20, -40,  -5,  -5,  -5,  -5, -40, -20],
              [120, -20,  20,   10,   10,  20, -20, 120]
              ]

def Eval_using_score_board(board,computerTile,playerTile):
    score = 0
    return huong(board, computerTile)
    #scoreStable = DiscStable(board)
    #for i in range(0,8):
    #    for j in range(0,8):
    #        if board[i][j] != computerTile and board[i][j] != playerTile:
    #            continue
    #        if board[i][j] == computerTile:
    #            score += scoreBoard[i][j]
    #        else:
    #            score -= scoreBoard[i][j]
    
    #return score+120*(scoreStable[computerTile]-scoreStable[playerTile])
def getNewBoard():
    board = []
    for i in range(8):
        board.append([-1] * 8)
    return board
def isStable(board,x,y):
    if (x==0 and y==0)or(x==0 and y==7)or(x==7 and y==0)or(x==7 and y==7):
        return True
    else:
        if board[x][y]==1:
            oTile = 2
        else:
            oTile = 1
        if x==0:
            y0 = y-1
            isSame1 = 1
            while y0!=-1:
                if board[x][y0]==-1:
                    isSame1 = -1
                    break
                elif  board[x][y0]== oTile:
                    isSame1 = 0                    
                else:
                    isSame1 =isSame1
                y0 = y0-1
            y1 = y+1
            isSame2 = 1
            while y1!=8:
                if board[x][y1]==-1:
                    isSame2 = -1
                    break
                elif  board[x][y1]== oTile:
                    isSame2 = 0                    
                else:
                    isSame2 =isSame2
                y1 = y1+1
            if isSame1+isSame2 >= 0:
                return True
            else:
                return False
        elif x == 7:
            y0 = y-1
            isSame1 = 1
            while y0!=-1:
                if board[x][y0]==-1:
                    isSame1 = -1
                    break
                elif  board[x][y0]== oTile:
                    isSame1 = 0                    
                else:
                    isSame1 =isSame1
                y0 = y0-1
            y1 = y+1
            isSame2 = 1
            while y1!=8:
                if board[x][y1]==-1:
                    isSame2 = -1
                    break
                elif  board[x][y1]== oTile:
                    isSame2 = 0                    
                else:
                    isSame2 =isSame2
                y1 = y1+1
            if isSame1+isSame2 >= 0:
                return True
            else:
                return False
        elif y == 0:
            x0 = x-1
            isSame1 = 1
            while x0!=-1:
                if board[x0][y]==-1:
                    isSame1 = -1
                    break
                elif  board[x0][y]== oTile:
                    isSame1 = 0                    
                else:
                    isSame1 =isSame1
                x0 = x0-1
            x1 = x+1
            isSame2 = 1
            while x1!=8:
                if board[x1][y]==-1:
                    isSame2 = -1
                    break
                elif  board[x1][y]== oTile:
                    isSame2 = 0                    
                else:
                    isSame2 =isSame2
                x1 = x1+1
            if isSame1+isSame2 >= 0:
                return True
            else:
                return False
        elif y ==7:
            x0 = x-1
            isSame1 = 1
            while x0!=-1:
                if board[x0][y]==-1:
                    isSame1 = -1
                    break
                elif  board[x0][y]== oTile:
                    isSame1 = 0                    
                else:
                    isSame1 =isSame1
                x0 = x0-1
            x1 = x+1
            isSame2 = 1
            while x1!=8:
                if board[x1][y]==-1:
                    isSame2 = -1
                    break
                elif  board[x1][y]== oTile:
                    isSame2 = 0                    
                else:
                    isSame2 =isSame2
                x1 = x1+1
            if isSame1+isSame2 >= 0:
                return True
            else:
                return False
        else:
            #-----------Thang------------
            x0 = x-1
            isSame1 = 1
            while x0!=-1:
                if board[x0][y]==-1:
                    isSame1 = -1
                    break
                elif  board[x0][y]== oTile:
                    isSame1 = 0                    
                else:
                    isSame1 =isSame1
                x0 = x0-1
            x1 = x+1
            isSame2 = 1
            while x1!=8:
                if board[x1][y]==-1:
                    isSame2 = -1
                    break
                elif  board[x1][y]== oTile:
                    isSame2 = 0                    
                else:
                    isSame2 =isSame2
                x1 = x1+1
            thang = False
            if isSame1+isSame2 >= 0:
                thang = True
            else:
                thang = thang
            #------------- Ngang ---------------
            y0 = y-1
            isSame3 = 1
            while y0!=-1:
                if board[x][y0]==-1:
                    isSame3 = -1
                    break
                elif  board[x][y0]== oTile:
                    isSame3 = 0                    
                else:
                    isSame3 =isSame3
                y0 = y0-1
            y1 = y+1
            isSame4 = 1
            while y1!=8:
                if board[x][y1]==-1:
                    isSame4 = -1
                    break
                elif  board[x][y1]== oTile:
                    isSame4 = 0                    
                else:
                    isSame4 =isSame4
                y1 = y1+1
            ngang = False
            if isSame3+isSame4 >= 0:
                ngang =True
            else:
                ngang = ngang
            #---------------- Cheo Trai--------------------
            y0 = y-1
            x0 = x-1
            isSame5 = 1
            while y0!=-1 and x0!=-1:
                if board[x0][y0]==-1:
                    isSame5 = -1
                    break
                elif  board[x0][y0]== oTile:
                    isSame5 = 0                    
                else:
                    isSame5 =isSame5
                y0 = y0-1
                x0 = x0-1
            y1 = y+1
            x1 = x+1
            isSame6 = 1
            while y1!=8 and x1!=8:
                if board[x1][y1]==-1:
                    isSame6 = -1
                    break
                elif  board[x1][y1]== oTile:
                    isSame6 = 0                    
                else:
                    isSame6 =isSame6
                y1 = y1+1
                x1 = x1+1
            cheo1 = False
            if isSame5+isSame6 >= 0:
                cheo1 = True
            else:
                cheo1 =cheo1
            #------------Cheo Phai--------------------
            y0 = y-1
            x0 = x+1
            isSame7 = 1
            while y0!=-1 and x0!=8:
                if board[x0][y0]==-1:
                    isSame7 = -1
                    break
                elif  board[x0][y0]== oTile:
                    isSame7 = 0                    
                else:
                    isSame7 =isSame7
                y0 = y0-1
                x0 = x0+1
            y1 = y+1
            x1 = x-1
            isSame8 = 1
            while y1!=8 and x1!=-1:
                if board[x1][y1]==-1:
                    isSame8 = -1
                    break
                elif  board[x1][y1]== oTile:
                    isSame8 = 0                    
                else:
                    isSame8 =isSame8
                y1 = y1+1
                x1 = x1-1
            cheo2 = False
            if isSame7+isSame8 >= 0:
                cheo2 = True
            else:
                cheo2 =cheo2
            if thang and ngang and cheo1 and cheo2:
                return True
    return False
def DiscStable(board):
    One = 0
    Two = 0
    # Kiem quan co co dinh
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] ==-1:
                continue
            elif board[i][j]==1:
                if isStable(board, i, j):
                    One = One+1
            else:
                if isStable(board, i, j):
                    Two = Two+1
    return {1:One,2:Two}
def isValidMove(board, tile, xstart, ystart):
    if board[xstart][ystart] != -1 or not isOnBoard(xstart, ystart):
        return False
    board[xstart][ystart] = tile # temporarily set the tile on the board.
    if tile == 1:
        otherTile = 2
    else:
        otherTile = 1
    tilesToFlip = []
    for xdirection, ydirection in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            # There is a piece belonging to the other player next to our piece.
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y): # break out of while loop, then continue in for loop
                    break
            if not isOnBoard(x, y):
                continue
            if board[x][y] == tile:
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    board[xstart][ystart] = -1 # restore the empty space
    if len(tilesToFlip) == 0: # If no tiles were flipped, this is not a valid move.
        return False
    return tilesToFlip

def isOnBoard(x, y):
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def getValidMoves(board, tile):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != 1 and board[x][y] != 2:
                if isValidMove(board, tile, x, y) != False:
                    validMoves.append([x, y])
    return validMoves

def getScoreOfBoard(board):
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 1:
                xscore += 1
            if board[x][y] == 2:
                oscore += 1
    return {1:xscore, 2:oscore}

def makeMove1(board, tile, xstart, ystart):
    tilesToFlip = isValidMove(board, tile, xstart, ystart)
    if tilesToFlip == False:
        return False
    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    dupeBoard = getNewBoard()
    for x in range(8):
        for y in range(8):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def isOnCorner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)
def getNextMove(board,tile,death,alpha,beta,computerTile,playerTile):
    MAXVALUE = 9999999
    MINVALUE = -MAXVALUE
    if death == 0:
        #return [-1,-1,getScoreOfBoard(board)[computerTile]-getScoreOfBoard(board)[playerTile]]
        #return [-1,-1,EvaluateBoard(board, tile)]
        score = Eval_using_score_board(board,computerTile,playerTile)
        #print score
        return [-1,score]
    else:
        possibleMoves = getMoveValid(board, tile)
        bestMoveRow = -1;
        bestMoveColumn = -1;
        if len(possibleMoves)==0:
            if tile == computerTile:
                tile = playerTile
            else:
                tile = computerTile
            possibleMoves = getMoveValid(board, tile)
        if tile == computerTile:
            isMax = True
        else: 
            isMax = False
        if not isMax:
            bestValue = MAXVALUE
        else:
            bestValue = MINVALUE
        #print possibleMoves#,len(possibleMoves),isMax,bestValue,tile
        if len(possibleMoves)==0:
            '''
            score = getScoreOfBoard(board)
            if score[computerTile]   > score[playerTile]:
                if isMax: 
                    return [-1,-1,MAXVALUE]
                else:
                    return [-1,-1,MAXVALUE]
            else:
                if isMax: 
                    return [-1,-1,MINVALUE]
                else:
                    return [-1,-1,MINVALUE]
                    '''
            return [-1,-bestValue]
        random.shuffle(possibleMoves)
        for n in possibleMoves:
            #rowIndex = n[0]
            #columnIndex = n[1]
            #dupeBoard = getBoardCopy(board)
            dupeBoard = [x for x in board]
            #makeMove(dupeBoard, tile, rowIndex, columnIndex)
            mmkk(dupeBoard, tile, n)
            if tile == computerTile:
                currentValue = getNextMove(dupeBoard,playerTile, death-1, alpha, beta,computerTile,playerTile)[1]
            else:
                currentValue = getNextMove(dupeBoard,computerTile, death-1, alpha, beta,computerTile,playerTile)[1]
            #print currentValue,bestValue#,possibleMoves
            if isMax:
                if currentValue >= bestValue:
                    bestValue = currentValue
                    #bestMoveRow = rowIndex
                    #bestMoveColumn = columnIndex
                    bestMove = n
                    if bestValue >= alpha:
                        alpha = bestValue
                    if bestValue >= beta:
                        break
            else:
                if currentValue <= bestValue:
                    bestValue = currentValue
                    #bestMoveRow = rowIndex
                    #bestMoveColumn = columnIndex
                    bestMove = n
                    if bestValue <= beta:
                        beta = bestValue
                    if bestValue <= alpha:
                        break
        #resultX = bestMoveRow
        #resultY = bestMoveColumn
        return [bestMove,bestValue]    
def getComputerMove(board, computerTile):
    depth = 4
    score = getScoreOfBoard(board)
    if depth +score[1]+score[2] > 64:
        depth = 64 - (score[1]+score[2])
    if computerTile==1:
        playerTile = 2
    else:
        playerTile = 1
    move = getNextMove(board,computerTile,depth,-99999999,99999999,computerTile,playerTile)
    return [move[0],move[1]]

matran =[[1, 1, 2, 2, 2, 2, -1, 2],
         [1, 2, 2, 2, 2, 2, 2, 2],
         [1, 1, 2, 1, 1, 2, 2, 2],
         [2, 1, 1, 2, 2, 1, 2, 2],
         [2, 1, 1, 2, 2, 2, 2, 2],
         [2, 1, 2, 1, 2, 2, 2, 2], 
         [2, -1, 2, 2, 1, 1, 2, -1],
         [2, 2, 2, 2, 2, 2, 2, -1]
         ]
matran4 =[[1, 1, 2, 2, 2, 2, -1, 2],
         [1, 1, 2, 2, 2, 2, 2, 2],
         [1, 1, 1, 1, 1, 2, 2, 2],
         [2, 1, 1, 1, 2, 1, 2, 2],
         [2, 1, 1, 2, 1, 2, 2, 2],
         [2, 1, 2, 1, 2, 1, 2, 2], 
         [2, -1, 2, 2, 1, 1, 1, -1],
         [2, 2, 2, 2, 2, 2, 2, 1]
         ]
matran2 =[
         [2, 2, 2, 2, 2, 2,2,2],
         [2, 2, 2, 2, 2, 2, 2, 2],
         [1,-1,-1,-1,-1,-1,-1,-1],
         [1,-1,-1,-1,-1,-1,-1,-1],
         [1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1], 
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1]
         ]
#print isStable(matran,6, 1)
#print DiscStable(matran)
#print Eval_using_score_board(matran, 2, 1)
#print getValidMoves(matran4, 2)
#print getComputerMove(matran4, 2)


import glob
import os
for filename in glob.glob('_first/*.txt'):
    f = open(os.path.join(os.getcwd(), filename), 'r')
    v = f.readlines()
    board = v[0].split(', ')
    if len(v) > 1:
        continue
    board = [int(x) for x in board]
    print (filename)
    f.close()
    b, w = ggpp(board)
    if b+w < 20: depth = 3
    elif b+w < 40: depth = 6
    else: depth = 4
    _,score = getNextMove(board, 1, depth, -99999,99999, 1, 2)
    f = open(os.path.join(os.getcwd(), filename), 'a')
    f.writelines('\n' + str(score))
    f.close()
    print score
    #break

