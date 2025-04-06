import tkinter as tk
import random as rand
from enteties.Field import Field

class MineFieldMedium:
    def __init__(self, master):
        self.master = master
        self.width = 14
        self.height = 14
        self.field = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.mines = []
        self.flags = []
        self.flags_count = 40
        self.is_game_over = False
        self.is_game_won = False

    def set_mines(self, mines):
        pos = [(x, y) for x in range(self.width) for y in range(self.height)]

        mines = rand.sample(pos, self.flags_count)

        for mine in mines:
            print(f"Mine at {mine}")
            self.field[mine[1]][mine[0]].is_mine = True

    def create_field(self):
        print("Creating field")

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        ## Generoitu

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        self.master.update_idletasks()  # Ensure the window dimensions are updated

        for y in range(self.height):
            self.grid_frame.rowconfigure(y, weight=1)
        for x in range(self.width):
            self.grid_frame.columnconfigure(x, weight=1)

        # self.grid_frame.place(anchor=tk.CENTER)
        # self.grid_frame.place(x=x, y=y)

        ## Generoitu päättyy

        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(self.grid_frame,x, y)
                self.field[y][x].draw_field()

        self.set_mines(self.flags_count)

        while True:
            for y in range(self.height):
                for x in range(self.width):

                    if self.field[y][x].is_mine and self.field[y][x].is_opened:
                        self.grid_frame.destroy()
                        label4 = tk.Label(self.master,bg="lightgrey", text="You lost!")
                        label4.pack()

                