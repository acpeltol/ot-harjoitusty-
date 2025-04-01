import tkinter as tk
from Field import Field

class MineField:
    def __init__(self, master, width, height):
        self.master = master
        self.width = width
        self.height = height
        self.field = [[None for _ in range(width)] for _ in range(height)]
        self.mines = []
        self.is_game_over = False
        self.is_game_won = False

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.master.update_idletasks()  # Ensure accurate width and height of window

        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()

        x_position = (window_width) // 2
        y_position = (window_height) // 2

        self.grid_frame.place(x=x_position, y=y_position, anchor=tk.CENTER)

    def create_field(self):
        print("Creating field")
        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(self.grid_frame,x, y)
                self.field[y][x].draw_field()