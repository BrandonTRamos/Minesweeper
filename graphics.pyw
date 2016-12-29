
from tkinter import *
from tkinter import messagebox
def main():


    class MyButton:
        def __init__(self,coord):
            self.coord=coord
            self.button=Button(root,text=displayboard[coord[0]+1][coord[1]+1],width=2,command=lambda: runturn(self.coord)).grid(row=coord[0],column=coord[1])
   

    def create_minelist(boardsize):
        import random
        minelist = []
        while len(minelist) < 8:
            minerow = random.randint(1, (boardsize))
            minecol = random.randint(1, (boardsize))
            if [minerow, minecol] not in minelist:
                minelist.append([minerow, minecol])
        return minelist

    def build_gameboard(boardsize, minelist):
        gameboard = [[' ' for i in range(boardsize+2)] for k in range(boardsize+2)]
        for row in range(1, boardsize+1):
            for col in range(1, boardsize+1):
                minecount = 0
                for mine in minelist:
                    if (row == mine[0] or row + 1 == mine[0] or row - 1 == mine[0]) and (
                                col == mine[1] or col + 1 == mine[1] or col - 1 == mine[1]) and (
                        [row, col] not in minelist):
                        minecount += 1
                gameboard[row][col] =str(minecount)
            for mine in minelist:
                gameboard[mine[0]][mine[1]] = "x"
        return gameboard

    def reveal_board(move):
        print(minelist)
        move=[move[0]+1,move[1]+1]
        displayboard[move[0]][move[1]] = gameboard[move[0]][move[1]]
        if move in minelist:
            for mine in minelist:
                displayboard[mine[0]][mine[1]] = gameboard[mine[0]][mine[1]]

    def zero_search(displayboard, gameboard,move):
        scanlist=[]
        revealedlist=[]
        scanlist.append(move)
        while scanlist:
            newreveal = [[scanlist[0][0], scanlist[0][1]- 1], [scanlist[0][0] - 1, scanlist[0][1] - 1], [scanlist[0][0] - 1, scanlist[0][1]], [scanlist[0][0] + 1, scanlist[0][1] - 1], [scanlist[0][0] + 1, scanlist[0][1]],
                         [scanlist[0][0] + 1, scanlist[0][1] + 1], [scanlist[0][0], scanlist[0][1] + 1], [scanlist[0][0] - 1, scanlist[0][1] + 1]]
            for coord in newreveal:
                displayboard[coord[0]][coord[1]] = gameboard[coord[0]][coord[1]]
                if coord not in scanlist and coord not in revealedlist and gameboard[coord[0]][coord[1]]=='0':
                    scanlist.append(coord)
            revealedlist.append(scanlist[0])
            del scanlist[0]

    def runturn(move):
            reveal_board(move)
            if displayboard[move[0]+1][move[1]+1]=='0':
                zero_search(displayboard,gameboard,[move[0]+1,move[1]+1])
            graphics = [[MyButton([k,i]) for i in range(8)] for k in range (8)]
            if gameboard[move[0]+1][move[1]+1]=="x":
                 playagain = messagebox.askquestion("Game Over","You Hit a Mine. :( Play Again?")
                 if playagain=="no":
                    root.destroy()
                    quit()
                 else:
                     root.destroy()
                     main()



    boardsize=8
    minelist=create_minelist(boardsize)
    gameboard=build_gameboard(boardsize,minelist)
    root = Tk()
    root.wm_title("Minesweeper")
    displayboard=[[" " for i in range(boardsize+2)] for j in range(boardsize+2)]	
    graphics = [[MyButton([k,i]) for i in range(8)] for k in range (8)]
    root.mainloop()
main()
