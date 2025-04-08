# pylint: disable=duplicate-code
import tkinter as tk
import random as rand
import sys
import time
from enteties.field import Field

class MineFieldHard:
    def __init__(self, master):
        self.master = master
        self.width = 20
        self.height = 20
        self.field = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.mines = []
        self.flags = []
        self.flags_count = 99

    def set_mines(self, mines):
        pos = [(x, y) for x in range(self.width) for y in range(self.height)]

        mines = rand.sample(pos, self.flags_count)

        for mine in mines:
            print(f"Mine at {mine}")
            self.field[mine[1]][mine[0]].is_mine = True

    def check_mines_blcok(self,x,y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0):
                    continue
                if (y + i < 0 or y + i >= self.height
                    or x + j < 0 or x + j >= self.width):
                    continue
                if self.field[y + i][x + j].is_mine is True:
                    count += 1
        self.field[y][x].mines_near_count = count

    def set_mines_near(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x].is_mine is True:
                    continue
                self.check_mines_blcok(x,y)

    def game_over(self):

        for y in range(self.height):
            for x in range(self.width):

                if self.field[y][x].is_mine is True and self.field[y][x].is_opened is True:
                    print("Destroy the window")
                    label4 = tk.Label(self.master,bg="lightgrey", text="You lost!")
                    label4.pack()
                    time.sleep(1)
                    sys.exit()

        self.master.after(100, self.game_over)

    def create_field(self):
        print("Creating field")

        self.grid_frame = tk.Frame(self.master)# pylint: disable=attribute-defined-outside-init
        self.grid_frame.pack(fill=tk.BOTH, expand=True)

        ## Generoitu

        self.master.update_idletasks()


        for y in range(self.height):
            self.grid_frame.rowconfigure(y, weight=1)
        for x in range(self.width):
            self.grid_frame.columnconfigure(x, weight=1)

        ## Generoitu päättyy

        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(self.grid_frame,x, y)
                self.field[y][x].draw_field()

        self.set_mines(self.flags_count)
        self.set_mines_near()

        self.master.after(100, self.game_over)
