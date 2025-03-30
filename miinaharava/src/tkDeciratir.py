import tkinter as tk
import time

class Tkdecorator():
    def __init__(self, master):
        # saldo on senteissä
        self.master = master

    def clear_window(self):
        for i in self.master.winfo_children():
            i.destroy()

    def start_game(self, difficulty):
        self.clear_window()

        self.master.configure(bg="darkblue")

        label4 = tk.Label(self.master,bg="lightblue", text="Peli alkaa!")
        label4.pack()

        time.sleep(1)

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

        self.master.geometry("800x600")

        self.master.configure(bg="lightgreen") 

        label2 = tk.Label(self.master,bg="lightgreen", text="Tervetuloa Miinaharava peliin!")
        label2.pack()

        start = tk.Button(self.master, text="Aloita peli", command=lambda: self.choose_difficulty())
        start.pack(pady=5)

        self.master.mainloop() 
