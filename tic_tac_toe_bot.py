
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeBot:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe vs Bot")
        self.player = "X"
        self.bot = "O"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_gui()

    def build_gui(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font='Arial 30', height=2, width=5,
                                command=lambda r=i, c=j: self.player_move(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def player_move(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.player
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "You Win!")
                self.reset()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset()
                return
            self.root.after(500, self.bot_move)

    def bot_move(self):
        empty = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]
        if not empty: return
        row, col = random.choice(empty)
        self.buttons[row][col]["text"] = self.bot
        if self.check_winner(self.bot):
            messagebox.showinfo("Game Over", "Bot Wins!")
            self.reset()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            self.reset()

    def check_winner(self, symbol):
        b = self.buttons
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] == symbol:
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] == symbol:
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] == symbol:
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] == symbol:
            return True
        return False

    def is_draw(self):
        return all(btn["text"] != "" for row in self.buttons for btn in row)

    def reset(self):
        for row in self.buttons:
            for btn in row:
                btn["text"] = ""

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeBot(root)
    root.mainloop()
