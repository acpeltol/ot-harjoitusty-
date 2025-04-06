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
    
    def draw_field(self):
        # print(f"Drawing field at ({self.x}, {self.y})")

        ## Osittain Generoitu

        # button = tk.Button(self.master, text="", width=2, height=1, command=lambda x=self.x, y=self.y: self.on_click())
        # button.bind("<Button-3>", self.on_right_click)
        # button.grid(row=self.y, column=self.x, padx=1, pady=1)

        self.button = tk.Button(self.master, text="", width=2, height=1, command=lambda x=self.x, y=self.y: self.on_click())
        self.button.bind("<Button-3>", self.on_right_click)
        self.button.grid(row=self.y, column=self.x, padx=1, pady=1, sticky="nsew")  # Make it expand to fill the grid cell

        # Osittain Generoitu päättyy

    def on_right_click(self, event):
        if self.is_opened:
            return
        if self.is_flagged:
            self.button.config(image="")
            self.button.image = None
            self.is_flagged = False
            print(f"Button ({self.x}, {self.y}) unflagged.")
        else:
            self.is_flagged = True
            self.image = ImageTk.PhotoImage(Image.open("src/images/flag.png").resize((50, 50)))
            self.button.config(image=self.image)
            self.button.image = self.image
            print(f"Button ({self.x}, {self.y}) flagged.")
        
        
    def on_click(self):
        if self.is_opened or self.is_flagged:
            return
        elif self.is_mine:
            self.image = ImageTk.PhotoImage(Image.open("src/images/mine.png").resize((50, 50)))
            self.button.config(image=self.image)
            self.button.image = self.image
            print(f"Game Over! Mine clicked ({self.x}, {self.y})")
        elif self.mines_near_count == 0:
            self.button.config(bg="lightgreen")
            self.button.bg = "lightgreen"

        self.is_opened = True
        print(f"Button {self.x}, {self.y}) clicked. Self.is_Mine: {self.is_mine}, self.is_opened: {self.is_opened}, self.is_flagged: {self.is_flagged}, self.mines_near_count: {self.mines_near_count}")
        