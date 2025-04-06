import tkinter as tk
import time
from enteties.MineFieldEasy import MineFieldEasy
from enteties.MineFieldMedium import MineFieldMedium
from enteties.MineFieldHard import MineFieldHard

class Tkdecorator():
    def __init__(self, master):
        self.master = master
        self.field = None

    def clear_window(self):
        for i in self.master.winfo_children():
            i.destroy()

    def start_game(self, difficulty):
        self.clear_window()

        self.master.configure(bg="lightgrey")

        label4 = tk.Label(self.master,bg="lightgrey", text="Peli alkaa!")
        label4.pack()

        if difficulty == 1:
            self.field = MineFieldEasy(self.master)
        elif difficulty == 2:
            self.field = MineFieldMedium(self.master)
        else:
            self.field = MineFieldHard(self.master)
        
        self.field.create_field()
        

    def choose_difficulty(self):
        self.clear_window()

        self.master.configure(bg="lightgreen")

        label3 = tk.Label(self.master,bg="lightgreen", text="Choose difficulty")
        label3.pack()

        button1 = tk.Button(self.master, text="Easy", command=lambda: self.start_game(1))
        button1.pack(pady=5)
        button2 = tk.Button(self.master, text="Middle", command=lambda: self.start_game(2))
        button2.pack(pady=5)
        button3 = tk.Button(self.master, text="Hard", command=lambda: self.start_game(3))
        button3.pack(pady=5)

    def decorate(self):
        self.master.title("Minesweeper")

        self.master.geometry("1200x1000")

        self.master.configure(bg="lightgreen") 

        label2 = tk.Label(self.master,bg="lightgreen", text="Tervetuloa Miinaharava peliin!")
        label2.pack()

        start = tk.Button(self.master, text="Aloita peli", command=lambda: self.choose_difficulty())
        start.pack(pady=5)

        self.master.mainloop() 
