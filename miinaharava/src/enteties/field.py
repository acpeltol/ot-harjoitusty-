import tkinter as tk
import pygame as pg
from PIL import Image, ImageTk


class Field:
    ' ' 'Class for creating one field and handeling the status of it' ' '
    def __init__(self, master, x, y, size, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.master = master
        self.is_mine = False
        self.is_opened = False
        self.is_flagged = False
        self.mines_near_count = 0
        self.image = ""
        self.size = size

    def draw_field(self):
        ' ' 'Drawing a field button and setting the size of it' ' '
        # Osittain Generoitu alkaa

        self.button = tk.Button(self.master, text="", width=2, height=1,
                                command=lambda x=self.x, y=self.y: self.on_click())
        self.button.bind("<Button-3>", self.on_right_click)
        self.button.grid(row=self.y, column=self.x,
                         padx=1, pady=1, sticky="nsew")

        # Osittain Generoitu päättyy

    def check_sound(self, many, file):
        ' ' 'Play the sound effect' ' '
        if many is False:
            pg.mixer.init()
            sound = pg.mixer.Sound(file)
            sound.play()

    def draw_button(self, image):
        ' ' 'Drawing the image on the button' ' '
        image = ImageTk.PhotoImage(Image.open(
                image).resize((self.size, self.size)))
        self.button.config(image=image)
        self.button.image = image


    def on_right_click(self, event):  # pylint: disable=unused-argument
        # Event handleri toimii kun on event atribuutti. Ilman sitä ei toimi
        ' ' 'Handling the right click event' ' '

        if self.is_opened:
            return
        if self.is_flagged:
            self.check_sound(False, "src/audio/minesweeper_dig_once.wav")

            self.button.config(image="")
            self.button.image = None

            self.is_flagged = False
            print(f"Button ({self.x}, {self.y}) unflagged.")
        else:
            if self.parent.flags_count == 0:
                return
            self.check_sound(False, "src/audio/minesweeper_dig_once.wav")
            self.is_flagged = True
            self.draw_button("src/images/flag.png")
            print(f"Button ({self.x}, {self.y}) flagged.")

    def on_click(self, many = False):
        ' ' 'Handling the left click event' ' '

        if self.is_opened or self.is_flagged:
            return
        if self.is_mine:

            self.check_sound(many, "src/audio/cinematic_explosion.wav")
            self.draw_button("src/images/mine.png")

        elif self.mines_near_count == 0:

            self.check_sound(many, "src/audio/minesweeper_dig_once.wav")

            self.button.config(bg="lightgreen")
            self.button.bg = "lightgreen"
        else:

            self.check_sound(many, "src/audio/minesweeper_dig_once.wav")

            names = ["one", "two", "three", "four",
                     "five", "six", "seven", "eight"]
            
            self.button.config(bg="lightgreen")
            #self.button.bg = "lightgreen"

            self.draw_button(f"src/images/{names[self.mines_near_count - 1]}.png")

        self.is_opened = True
