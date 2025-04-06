import tkinter as tk
import random as rand
from enteties.Field import Field

class MineFieldEasy:
    def __init__(self, master):
        self.master = master
        self.width = 8
        self.height = 8
        self.field = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.mines = []
        self.flags = []
        self.flags_count = 10
        self.is_game_over = False
        self.is_game_won = False

    def set_mines(self, mines):
        pos = [(x, y) for x in range(self.width) for y in range(self.height)]

        mines = rand.sample(pos, self.flags_count)

        for mine in mines:
            print(f"Mine at {mine}")
            self.field[mine[1]][mine[0]].is_mine = True

    def set_mines_near(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.field[y][x].is_mine:
                    continue

                ## Generoitu
                count = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if (i == 0 and j == 0) or (y + i < 0 or y + i >= self.height or x + j < 0 or x + j >= self.width):
                            continue
                        if self.field[y + i][x + j].is_mine:
                            count += 1
                self.field[y][x].mines_near_count = count

                ## Generoitu päättyy

    def game_over(self):

        for y in range(self.height):
                for x in range(self.width):

                    if self.field[y][x].is_mine == True and self.field[y][x].is_opened == True:
                        print("Game Over")
                        label4 = tk.Label(self.master,bg="lightgrey", text="You lost!")
                        label4.pack()
                        self.master.destroy()
                        return 
        return False

    def create_field(self):
        print("Creating field")

        self.grid_frame = tk.Frame(self.master)
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

        # while True:
        #     for y in range(self.height):
        #         for x in range(self.width):

        #             if self.field[y][x].is_mine == True and self.field[y][x].is_opened == True:
        #                 print("Game Over")
        #                 label4 = tk.Label(self.master,bg="lightgrey", text="You lost!")
        #                 label4.pack()
        #                 self.master.destroy()

        self.master.after(100, self.game_over)


