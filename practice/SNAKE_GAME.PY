"""
Snake Game with persistent Leaderboard
Single-file Python 3 Tkinter game.

Features:
- Classic snake movement with arrow keys (or WASD)
- Food spawning and score tracking
- Increasing speed as score grows
- Pause/Resume (Space)
- Restart (R)
- Persistent leaderboard stored in 'leaderboard.json' (top 10 scores)
- On game over, prompt player for name and store score

Run: python snake_leaderboard.py
"""

import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import json
import os
import time

# ---- Config ----
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 50
COLUMNS = WIDTH // CELL_SIZE
ROWS = HEIGHT // CELL_SIZE
INIT_LENGTH = 4
BASE_SPEED_MS = 200  # base delay between moves in milliseconds
SPEED_DECREASE_PER_POINT = 3  # ms faster per point (down to a min)
MIN_SPEED_MS = 40
LEADERBOARD_FILE = "leaderboard.json"
MAX_LEADERS = 10

# ---- Helpers for leaderboard persistence ----

def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    try:
        with open(LEADERBOARD_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        # validate
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []


def save_leaderboard(board):
    try:
        with open(LEADERBOARD_FILE, "w", encoding="utf-8") as f:
            json.dump(board, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Failed to save leaderboard:", e)


def update_leaderboard(name, score):
    board = load_leaderboard()
    board.append({"name": name, "score": score, "time": int(time.time())})
    board.sort(key=lambda x: x["score"], reverse=True)
    board = board[:MAX_LEADERS]
    save_leaderboard(board)
    return board

# ---- Game Class ----

class SnakeGame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Snake - Leaderboard Demo")
        self.pack()

        self.canvas = tk.Canvas(self, width=WIDTH, height=HEIGHT, bg="#111")
        self.canvas.grid(row=0, column=0, rowspan=6)

        # Sidebar for score and leaderboard
        self.side_frame = tk.Frame(self)
        self.side_frame.grid(row=0, column=1, sticky="n")

        self.score_var = tk.StringVar(value="Score: 0")
        self.score_label = tk.Label(self.side_frame, textvariable=self.score_var, font=("Consolas", 30))
        self.score_label.pack(pady=(6, 2))

        self.info_label = tk.Label(self.side_frame, text="Controls:\nArrows / WASD\nSpace: Pause\nR: Restart", justify="left")
        self.info_label.pack(pady=(0, 10))

        self.leader_label = tk.Label(self.side_frame, text="Leaderboard", font=("Consolas", 12, "bold"))
        self.leader_label.pack()

        self.leader_text = tk.Text(self.side_frame, width=24, height=16, state="disabled", bg="#222", fg="#ddd")
        self.leader_text.pack(padx=4, pady=4)

        # Bind controls
        self.master.bind('<KeyPress>', self.on_key_press)

        self.reset_game()
        self.draw_board()
        self.refresh_leaderboard_display()

        # Start mainloop
        self.running = True
        self.after(self.speed_ms, self.game_step)

    def reset_game(self):
        self.direction = (1, 0)  # moving right
        self.next_direction = self.direction
        start_x = COLUMNS // 4
        start_y = ROWS // 2
        self.snake = [(start_x - i, start_y) for i in range(INIT_LENGTH)]
        self.spawn_food()
        self.score = 0
        self.update_score_label()
        self.game_over = False
        self.paused = False
        self.speed_ms = BASE_SPEED_MS

    def spawn_food(self):
        while True:
            x = random.randint(0, COLUMNS - 1)
            y = random.randint(0, ROWS - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def draw_board(self):
        self.canvas.delete("all")
        # draw food
        fx, fy = self.food
        self.draw_cell(fx, fy, fill="#e74c3c")
        # draw snake
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                self.draw_cell(x, y, fill="#2ecc71")
            else:
                self.draw_cell(x, y, fill="#27ae60")

    def draw_cell(self, grid_x, grid_y, fill="#fff"):
        x1 = grid_x * CELL_SIZE
        y1 = grid_y * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, outline="#000", fill=fill)

    def on_key_press(self, event):
        key = event.keysym
        if key in ("Left", "a", "A"):
            self.try_change_direction((-1, 0))
        elif key in ("Right", "d", "D"):
            self.try_change_direction((1, 0))
        elif key in ("Up", "w", "W"):
            self.try_change_direction((0, -1))
        elif key in ("Down", "s", "S"):
            self.try_change_direction((0, 1))
        elif key == "space":
            self.toggle_pause()
        elif key in ("r", "R"):
            self.restart()

    def try_change_direction(self, new_dir):
        # prevent reversing
        dx, dy = new_dir
        cdx, cdy = self.direction
        if (dx == -cdx and dy == -cdy):
            return
        # store as next direction so fast key presses don't break movement
        self.next_direction = new_dir

    def toggle_pause(self):
        if self.game_over:
            return
        self.paused = not self.paused
        if not self.paused:
            self.after(self.speed_ms, self.game_step)

    def restart(self):
        if messagebox.askyesno("Restart", "Restart the game?"):
            self.reset_game()
            self.draw_board()

    def game_step(self):
        if self.paused or self.game_over:
            return
        # apply next direction
        self.direction = self.next_direction
        head_x, head_y = self.snake[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # check collisions
        if self.check_collision(new_head):
            self.on_game_over()
            return

        # move snake
        self.snake.insert(0, new_head)
        # check food
        if new_head == self.food:
            self.score += 1
            self.update_score_label()
            self.spawn_food()
            # speed up a bit
            self.speed_ms = max(MIN_SPEED_MS, BASE_SPEED_MS - self.score * SPEED_DECREASE_PER_POINT)
        else:
            self.snake.pop()

        self.draw_board()
        self.after(self.speed_ms, self.game_step)

    def check_collision(self, head):
        x, y = head
        # wall collision
        if x < 0 or x >= COLUMNS or y < 0 or y >= ROWS:
            return True
        # self collision
        if head in self.snake:
            return True
        return False

    def on_game_over(self):
        self.game_over = True
        self.draw_board()
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 - 20, text="GAME OVER", fill="#fff", font=("Consolas", 28, "bold"))
        self.canvas.create_text(WIDTH // 2, HEIGHT // 2 + 10, text=f"Score: {self.score}", fill="#ddd", font=("Consolas", 18))

        # prompt player for name
        name = simpledialog.askstring("Game Over", f"Your score: {self.score}\nEnter your name for the leaderboard:")
        if name:
            board = update_leaderboard(name.strip() or "Anonymous", self.score)
            self.refresh_leaderboard_display(board)
        else:
            # still refresh (maybe scores changed)
            self.refresh_leaderboard_display()

    def update_score_label(self):
        self.score_var.set(f"Score: {self.score}")

    def refresh_leaderboard_display(self, board=None):
        if board is None:
            board = load_leaderboard()
        self.leader_text.config(state="normal")
        self.leader_text.delete("1.0", tk.END)
        if not board:
            self.leader_text.insert(tk.END, "<no scores yet>\n")
        else:
            for i, entry in enumerate(board, start=1):
                name = entry.get("name", "?")
                sc = entry.get("score", 0)
                ts = entry.get("time", 0)
                self.leader_text.insert(tk.END, f"{i:2d}. {name:12.12s}  {sc:4d}\n")
        self.leader_text.config(state="disabled")


# ---- Launcher ----

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.protocol("WM_DELETE_WINDOW", root.quit)
    root.mainloop()

if __name__ == '__main__':
    main()
