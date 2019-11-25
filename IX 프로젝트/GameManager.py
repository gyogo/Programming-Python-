import tkinter
from tkinter import messagebox
import math
from tictactoe import TicTacToe


class GameManager:
    def __init__(self):
        self.ttt = TicTacToe()
        self.images=dict(0)
    def play(self):
        # 게임판 보여주자
        print(self.ttt)
        while True:
            # row, col 입력받자
            row = int(input("row : "))
            col = int(input("col :"))
            self.ttt.set(row, col)
            self.ttt.set(1, 1)
            print(self.ttt)

            # check_winner 면 끝내자
            if self.ttt.check_winner() == "O":
                print("O win!!!")
                break
            elif self.ttt.check_winner() == "X":
                print("X win!!!")
                break
            elif self.ttt.check_winner() == "d":
                print("무승부")
                break
class Gamaneger_GUI:
    def
        CANVAS_SIZE=300
        self.TILE.SIZE=CANVAS_SIZE/3

        self.root = tkinter.TK()
        self.root.title("틱택토")
        self.root.geometry(str(CANVAS_SIZE)+"x"+str(CANVAS_SIZE)) #300x300
        self.root.resizable(width=False, height=False) #창크기 변경 ㄴㄴ
        self.canvas = tkinter.Canvas(self.root,bg="white",width=CANVAS_SIZE,height=CANVAS_SIZE)
        self.canvas.pack()


     self.root.mainloop()

if _name_ == '_main_':
    gm = GameManager_GUI()
    gm.play()