# pylint: disable=duplicate-code
# Tarvitaan muutama samanlainen teidosto mahdollisia integraatioita varten
import tkinter as tk
import time
import pygame as pg
from enteties.field import Field
from enteties.filed_start import FieldStart


class MineFieldMedium:
    def __init__(self, master, width, height, image_size, flags_count):
        self.master = master
        self.width = width
        self.height = height
        self.field = [[None for _ in range(self.width)]
                      for _ in range(self.height)]
        self.mines = set()
        self.flags = set()
        self.flags_count = flags_count
        self.image_size = image_size
        self.field_start = FieldStart(self)

    def check_flagged(self, x, y):
        if self.field[y][x].is_flagged is True:
            if (x, y) in self.flags:
                return
            self.flags.add((x, y))
            self.flags_count -= 1
            print(self.flags)
        else:
            if (x, y) not in self.flags:
                return
            self.flags.remove((x, y))
            self.flags_count += 1
            print(self.flags)

    def game_status(self):

        opened_count = 0

        for y in range(self.height):
            for x in range(self.width):

                if self.field[y][x].is_mine is True and self.field[y][x].is_opened is True:
                    print("Destroy the window")
                    # pg.mixer.init()
                    # sound = pg.mixer.Sound("src/audio/cinematic_explosion.wav")
                    # sound.play()
                    time.sleep(1)
                    label = tk.Label(self.master, bg="lightgrey",
                                     text="You Lost!", font=("Arial", 20))
                    label.place(relx=0.5, rely=0.5, anchor='center')
                    self.master.after(2000, self.master.quit)

                self.check_flagged(x, y)

                if (self.field[y][x].is_opened is True) and (self.field[y][x].mines_near_count == 0) and ((y, x) not in self.field_start.explosion_count):
                    print(f"Explosion open {x}, {y}")
                    self.field_start.open_fields((x, y))

                if self.field[y][x].is_opened is True:
                    opened_count += 1

        if opened_count == self.width * self.height - len(self.mines):
            print("You won!")
            time.sleep(1)
            label = tk.Label(self.master, bg="lightgrey",
                             text="You won!", font=("Arial", 20))
            label.place(relx=0.5, rely=0.5, anchor='center')
            self.master.after(2000, self.master.quit)

        self.master.after(100, self.game_status)

    def after_field_created(self):
        print("Field created")
        self.game_status()

    def create_field(self):
        print("Creating field")

        grid_frame = tk.Frame(self.master)
        grid_frame.pack(fill=tk.BOTH, expand=True)

        # Generoitu

        self.master.update_idletasks()

        for y in range(self.height):
            grid_frame.rowconfigure(y, weight=1)
        for x in range(self.width):
            grid_frame.columnconfigure(x, weight=1)

        # Generoitu päättyy

        for y in range(self.height):
            for x in range(self.width):

                self.field[y][x] = Field(grid_frame, x, y, self.image_size)
                self.field[y][x].draw_field()

        self.field_start.start(self.after_field_created)
