
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.build_gui()

    def build_gui(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text="", font='Arial 30', height=2, width=5,
                                command=lambda r=i, c=j: self.on_click(r, c))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

    def on_click(self, row, col):
        btn = self.buttons[row][col]
        if btn["text"] == "":
            btn["text"] = self.player
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.player} wins!")
                self.reset()
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        b = self.buttons
        for i in range(3):
            if b[i][0]["text"] == b[i][1]["text"] == b[i][2]["text"] != "":
                return True
            if b[0][i]["text"] == b[1][i]["text"] == b[2][i]["text"] != "":
                return True
        if b[0][0]["text"] == b[1][1]["text"] == b[2][2]["text"] != "":
            return True
        if b[0][2]["text"] == b[1][1]["text"] == b[2][0]["text"] != "":
            return True
        return False

    def is_draw(self):
        return all(btn["text"] != "" for row in self.buttons for btn in row)

    def reset(self):
        for row in self.buttons:
            for btn in row:
                btn["text"] = ""
        self.player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
