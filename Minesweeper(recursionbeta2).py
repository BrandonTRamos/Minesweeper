import os 
import sys
sys.setrecursionlimit(5000)
def create_minelist(boardsize,nummines):
    import random
    minelist = []
    while len(minelist) < nummines:
        minerow = random.randint(1, boardsize)
        minecol = random.randint(1, boardsize)
        if [minerow, minecol] not in minelist:
            minelist.append([minerow, minecol])
    return minelist



def build_gameboard(boardsize, minelist):
    gameboard = [['[ ]' for i in range(boardsize+2)] for k in range(boardsize+2)]
    for row in range(1, boardsize+1):
        for col in range(1, boardsize+1):
            minecount = 0
            for mine in minelist:
                if (row == mine[0] or row + 1 == mine[0] or row - 1 == mine[0]) and (
                            col == mine[1] or col + 1 == mine[1] or col - 1 == mine[1]) and (
                    [row, col] not in minelist):
                    minecount += 1
            gameboard[row][col] = '[' + str(minecount) + ']'
        for mine in minelist:
            gameboard[mine[0]][mine[1]] = '[x]'
    return gameboard


def print_displayboard(displayboard,boardsize):
    top='     '
    for i in range(1,boardsize+1):
        top+=' '+str(i).ljust(2)
    print(top)
    print('     ',('|  ')*boardsize)
    for i in range(boardsize):
        print (str(i+1).rjust(2),'-',''.join(displayboard[i+1][1:boardsize+1]),'-',str(i+1).ljust(2))
    print('     ',('|  ')*boardsize)
    print(top)
    print('\n')


def reveal_board(displayboard, gameboard, minelist, movelist,boardsize):
    while True:
        os.system('cls')
        print_displayboard(displayboard,boardsize)
        inputrow = input('\nReveal Row: ')
        inputcol = input('Reveal col: ')
        move=[int(inputrow), int(inputcol)]
        if move in movelist:
            print("Square already revealed.\n")
        else:
            break
    print('\n')
    movelist.append(move)
    if gameboard[move[0]][move[1]]!='[0]':
        displayboard[move[0]][move[1]] = gameboard[move[0]][move[1]]
    if move in minelist:
        os.system('cls')
        for mine in minelist:
            displayboard[mine[0]][mine[1]] = gameboard[mine[0]][mine[1]]
        print_displayboard(displayboard,boardsize)
        print('Game Over: You hit a mine. \n')
        a = input('\nPlay again?(y/n):')
        if a == 'y':
            os.system('cls')
            rungame()
        else:
            sys.exit()
    return move


def zero_search(gameboard,displayboard,row,col,zeroslist):
        newsearch = [[row, col - 1], [row - 1, col - 1], [row - 1, col], [row + 1, col - 1], [row + 1, col],
                     [row + 1, col + 1], [row, col + 1], [row - 1, col + 1]]
        if gameboard[row][col]=='[0]':
            zeroslist.append((row,col))
            displayboard[row][col]=gameboard[row][col]
            for element in newsearch:
                if displayboard[element[0]][element[1]]=='[ ]':
                    displayboard[element[0]][element[1]] = gameboard[element[0]][element[1]]
        for i in range(8):
            if gameboard[newsearch[i][0]][newsearch[i][1]] == '[0]' and (newsearch[i][0],newsearch[i][1]) not in zeroslist:
                zeroslist.append((newsearch[i][0],newsearch[i][1]))
                zero_search(gameboard,displayboard,newsearch[i][0],newsearch[i][1],zeroslist)


def wincheck(displayboard, boardsize, minelist):
    revealedcount = 0
    for row in range(1, boardsize+1):
        for col in range(1, boardsize+1):
            if displayboard[row][col] != '[ ]' and displayboard[row][col] != '[F]':
                revealedcount += 1
    if revealedcount == (boardsize ** 2) - len(minelist):
        os.system('cls')
        print('\n You Won!\n')
        print_displayboard(displayboard, boardsize)
        a = input('Play again?(y/n):')
        if a == 'y':
            os.system('cls')
            rungame()
        else:
            sys.exit()


def flag_square(displayboard):
    flagRow = input('Flag Row: ')
    flagCol = input('Flag col: ')
    displayboard[int(flagRow) - 1][int(flagCol) - 1] = '[F]'
    os.system('cls')

def rungame():
    boardsize = int(input("Board size:"))
    nummines=int(input('Number of mines:'))
    movelist = []
    minelist = create_minelist(boardsize,nummines)
    displayboard = [['[ ]' for i in range(boardsize+2)] for k in range(boardsize+2)]
    gameboard = build_gameboard(boardsize,minelist)
	
    while True:
        zeroslist=[]
        move=reveal_board(displayboard,gameboard,minelist,movelist,boardsize)
        zero_search(gameboard,displayboard,move[0],move[1],zeroslist)
        wincheck(displayboard,boardsize,minelist)
        os.system('cls')
        print_displayboard(displayboard,boardsize)


        while True:
            flagcheck = input('\nDo you want to flag a square(y/n)? ')
            if flagcheck == 'y':
                flag_square(displayboard)
                print_displayboard(displayboard,boardsize)
            else:
                break
rungame()
