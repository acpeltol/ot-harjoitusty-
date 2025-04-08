import tkinter as tk
from PIL import Image, ImageTk

class Field:
    def __init__(self, master, x, y):
        self.x = x
        self.y = y
        self.master = master
        self.is_mine = False
        self.is_opened = False
        self.is_flagged = False
        self.mines_near_count = 0
        self.image = ""

    def draw_field(self):
        # Osittain Generoitu alkaa

        self.button = tk.Button(self.master, text="", width=2, height=1, # pylint: disable=attribute-defined-outside-init
                                command=lambda x=self.x, y=self.y: self.on_click())
        self.button.bind("<Button-3>", self.on_right_click)
        self.button.grid(row=self.y, column=self.x, padx=1, pady=1, sticky="nsew")

        # Osittain Generoitu päättyy

    def on_right_click(self, event): # pylint: disable=unused-argument
        if self.is_opened:
            return
        if self.is_flagged:
            self.button.config(image="")
            self.button.image = None
            self.is_flagged = False
            print(f"Button ({self.x}, {self.y}) unflagged.")
        else:
            self.is_flagged = True
            image = ImageTk.PhotoImage(Image.open("src/images/flag.png").resize((100, 100)))
            self.button.config(image=image)
            self.button.image = image
            print(f"Button ({self.x}, {self.y}) flagged.")


    def on_click(self):
        if self.is_opened or self.is_flagged:
            return
        if self.is_mine:
            image = ImageTk.PhotoImage(Image.open("src/images/mine.png").resize((100, 100)))
            self.button.config(image=image)
            self.button.image = image

        elif self.mines_near_count == 0:
            self.button.config(bg="lightgreen")
            self.button.bg = "lightgreen"

        self.is_opened = True
        print(f'''Button {self.x}, {self.y}) clicked. Self.is_Mine: {self.is_mine},
              self.is_opened: {self.is_opened}, self.is_flagged: {self.is_flagged},
              self.mines_near_count: {self.mines_near_count}''')
