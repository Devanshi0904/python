"""
Tic Tac Toe 3.0 (BIG UI VERSION)
Modern Tkinter design with:
- Player vs Player or Player vs Computer (AI)
- Unbeatable AI using Minimax
- Bigger buttons, larger text, and glowing color theme
"""

import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe 3.0 — Big Version")
        self.master.config(bg="#101820")
        self.master.resizable(False, False)

        self.current_player = "X"
        self.vs_computer = False
        self.board = ["" for _ in range(9)]

        # Title
        self.title_label = tk.Label(master, text="TIC TAC TOE", font=("Consolas", 20, "bold"), fg="#00ffcc", bg="#101820")
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(20, 10))

        # Status
        self.status_label = tk.Label(master, text="Choose Mode", font=("Consolas", 20), fg="#ffffff", bg="#101820")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))

        # Mode Buttons
        self.pvp_btn = tk.Button(master, text="Player vs Player", command=self.start_pvp,
                                 font=("Consolas", 18, "bold"), bg="#00b894", fg="white", width=18, height=1)
        self.pvp_btn.grid(row=2, column=0, columnspan=3, pady=10)

        self.ai_btn = tk.Button(master, text="Player vs Computer", command=self.start_ai,
                                font=("Consolas", 18, "bold"), bg="#0984e3", fg="white", width=18, height=1)
        self.ai_btn.grid(row=3, column=0, columnspan=3, pady=10)

        # Game Buttons
        self.buttons = []
        for i in range(9):
            btn = tk.Button(master, text="", width=8, height=3, font=("Consolas", 20, "bold"),
                            bg="#2d3436", fg="#dfe6e9", activebackground="#636e72",
                            command=lambda i=i: self.make_move(i))
            row, col = divmod(i, 3)
            btn.grid(row=row + 4, column=col, padx=10, pady=10)
            self.buttons.append(btn)

        # Reset
        self.reset_button = tk.Button(master, text="Restart", command=self.reset_game,
                                      font=("Consolas", 18, "bold"), bg="#d63031", fg="white", width=12, height=1)
        self.reset_button.grid(row=7, column=0, columnspan=3, pady=20)

    # ------------------------ Modes ------------------------
    def start_pvp(self):
        self.vs_computer = False
        self.reset_game()
        self.status_label.config(text="Player X's Turn")

    def start_ai(self):
        self.vs_computer = True
        self.reset_game()
        self.status_label.config(text="You are X. Computer is O.")

    # ------------------------ Moves ------------------------
    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            color = "#00cec9" if self.current_player == "X" else "#fd79a8"
            self.buttons[index].config(text=self.current_player, state="disabled", bg=color)

            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} Wins!")
                messagebox.showinfo("Game Over", f"Player {self.current_player} Wins!")
                self.disable_all_buttons()
            elif "" not in self.board:
                self.status_label.config(text="It's a Draw!")
                messagebox.showinfo("Game Over", "It's a Draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.vs_computer and self.current_player == "O":
                    self.master.after(500, self.ai_move)
                else:
                    self.status_label.config(text=f"Player {self.current_player}'s Turn")

    # ------------------------ AI ------------------------
    def ai_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i
        if best_move is not None:
            self.make_move(best_move)

    def minimax(self, is_maximizing):
        winner = self.get_winner()
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif "" not in self.board:
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = ""
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.board[i] == "":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = ""
                    best_score = min(best_score, score)
            return best_score

    # ------------------------ Helpers ------------------------
    def get_winner(self):
        combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in combos:
            if self.board[a] == self.board[b] == self.board[c] != "":
                for i in (a, b, c):
                    self.buttons[i].config(bg="#f1c40f")
                return self.board[a]
        return None

    def check_winner(self):
        return self.get_winner() is not None

    def disable_all_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#2d3436")
        if self.vs_computer:
            self.status_label.config(text="You are X. Computer is O.")
        else:
            self.status_label.config(text="Player X's Turn")


# ------------------------ Run ------------------------
if __name__ == "__main__":
    root = tk.Tk()
    TicTacToe(root)
    root.mainloop()
