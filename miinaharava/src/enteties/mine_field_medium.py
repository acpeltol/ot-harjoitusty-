import tkinter as tk
import time
from enteties.field import Field
from enteties.filed_start import FieldStart


class MineFieldMedium:
    ' ' 'Class for creating a mine field and handeling game status' ' '
    def __init__(self, master, width, height, image_size, flags_count, parent):
        self.master = master
        self.width = width
        self.height = height
        self.parent = parent
        self.field = [[None for _ in range(self.width)]
                      for _ in range(self.height)]
        self.mines = set()
        self.flags = set()
        self.flags_count = flags_count
        self.image_size = image_size
        self.field_start = FieldStart(self)
        self.game_goig = True
        self.flag_label = None

    def check_flagged(self, x, y):
        ' ' 'Checking if certain field is flagged and update the information in the class' ' '
        if self.field[y][x].is_flagged is True:
            if (x, y) in self.flags:
                return
            self.flags.add((x, y))
            self.flags_count -= 1
        else:
            if (x, y) not in self.flags:
                return
            self.flags.remove((x, y))
            self.flags_count += 1

        self.draw_flag_count(True)

    def check_if_empty_field(self, x, y):
        ' ' 'Checking if certain field is empty and call another function to open fields nearby' ' '
        if self.field[y][x].is_opened is False:
            return
        if self.field[y][x].mines_near_count != 0:
            return
        if (x, y) in self.field_start.explosion_count:
            return
        if self.field[y][x].is_mine is True:
            return

        self.field_start.open_fields((x, y))

    def check_vicotry(self, count):
        ' ' 'Checking if the game is won' ' '
        if count == self.width * self.height - len(self.mines):
            print("You won!")
            self.game_goig = False
            label = tk.Label(self.master, bg="lightgrey",
                             text="You won!", font=("Arial", 20))
            label.place(relx=0.5, rely=0.5, anchor='center')
            time.sleep(2)
            self.parent.choose_difficulty()

    def chekc_loose(self, x, y):
        ' ' 'Checking if the game is lost' ' '
        if self.field[y][x].is_mine is True and self.field[y][x].is_opened is True:
            print("Destroy the window")
            self.game_goig = False
            time.sleep(1)
            label = tk.Label(self.master, bg="lightgrey",
                             text="You Lost!", font=("Arial", 20))
            label.place(relx=0.5, rely=0.5, anchor='center')
            time.sleep(2)
            self.parent.choose_difficulty()

    def game_status(self):
        ' ' 'Checking the game status by looping the state of every field' ' '

        opened_count = 0

        for y in range(self.height):
            for x in range(self.width):

                self.chekc_loose(x, y)

                self.check_flagged(x, y)

                self.check_if_empty_field(x, y)

                if self.field[y][x].is_opened is True:
                    opened_count += 1

        self.check_vicotry(opened_count)

        if self.game_goig is False:
            return

        self.master.after(100, self.game_status)

    def draw_flag_count(self, being=False):
        ' ' 'Drawing the flag count on the screen' ' '

        if being is False:
            # Genoroitu alkaa
            self.flag_label = tk.Label(self.master, text=f"Flags: {self.flags_count}", font=("Arial", 14))
            self.flag_label.pack(pady=(5, 0))  # top padding only
            # Genoroitu päättyy
        else:
            self.flag_label.config(text=f"Flags: {self.flags_count}")
            self.flag_label.update_idletasks()

    def create_field(self):
        print("Creating field")

        # Generoitu alkaa

        self.draw_flag_count()

        grid_frame = tk.Frame(self.master)
        grid_frame.pack(fill=tk.BOTH, expand=True)

        self.master.update_idletasks()

        for y in range(self.height):
            grid_frame.rowconfigure(y, weight=1)
        for x in range(self.width):
            grid_frame.columnconfigure(x, weight=1)

        # Generoitu päättyy

        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(grid_frame, x, y, self.image_size, self)
                self.field[y][x].draw_field()

        # self.field_start.start(self.after_field_created)
        self.field_start.start(self.game_status)
