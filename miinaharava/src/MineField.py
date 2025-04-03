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

    def create_field(self):
        print("Creating field")

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        ## Generoitu

        self.master.update_idletasks()  

        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()

        x = (window_width) // 2
        y = (window_height) // 2

        self.grid_frame.place(x=x, y=y, anchor=tk.CENTER)

        ## Generoitu päättyy

        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(self.grid_frame,x, y)
                self.field[y][x].draw_field()