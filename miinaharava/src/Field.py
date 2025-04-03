import tkinter as tk

class Field:
    def __init__(self, master, x, y):
        self.x = x
        self.y = y
        self.master = master
        self.is_mine = False
        self.is_opened = False
        self.is_flagged = False
        self.adjacent_mines_count = 0
    
    def draw_field(self):
        print(f"Drawing field at ({self.x}, {self.y})")

        ## Generoitu

        button = tk.Button(self.master, text="", width=3, height=1, command=lambda x=self.x, y=self.y: self.on_click())
        button.grid(row=self.y, column=self.x, padx=1, pady=1)

        # Generoitu päättyy

        # self.button = tk.Button(self.grid_frame, text="", width=1, height=1, command=self.on_click)
        # self.button.grid(row=self.y, column=self.x, padx=1, pady=1)

    def on_click(self):
        print(f"Button at ({self.x}, {self.y}) clicked.")
        