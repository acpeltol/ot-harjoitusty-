import tkinter as tk
from enteties.mine_field_medium import MineFieldMedium

class Tkdecorator():
    ' ' 'Class for creating a tkinter window and start the game' ' '
    def __init__(self, master):
        self.master = master
        self.field = None

    def clear_window(self):
        ' ' 'Clear the window' ' '
        for i in self.master.winfo_children():
            i.destroy()

    def start_game(self, difficulty):
        ' ' 'Start the game and create a mine field' ' '
        self.clear_window()

        self.master.configure(bg="lightgrey")

        label4 = tk.Label(self.master, bg="lightgrey", text="Peli alkaa!")
        label4.pack()

        if difficulty == 1:
            self.field = MineFieldMedium(self.master, 8, 8, 100,10,self)
        elif difficulty == 2:
            self.field = MineFieldMedium(self.master, 14, 14, 60, 40,self)
        else:
            self.field = MineFieldMedium(self.master, 17, 17, 50, 60, self)

        self.field.create_field()

    def draw_button(self, text,difficulty):
        ' ' 'Draw the button' ' '

        button1 = tk.Button(self.master, text=text,
                            command=lambda: self.start_game(difficulty))
        button1.pack(pady=5)

    def draw_label(self, text):
        ' ' 'Draw the label' ' '

        label3 = tk.Label(self.master, bg="lightgreen",
                          text=text)
        label3.pack()


    def choose_difficulty(self):
        ' ' 'Drawing window to choose the difficulty of the game' ' '
        self.clear_window()

        self.master.configure(bg="lightgreen")

        self.draw_label("Choose difficulty")

        self.draw_button("Easy",1)

        self.draw_label("8x8, 10 mines")

        self.draw_button("Medium",2)

        self.draw_label("14x14, 40 mines")

        self.draw_button("Hard",3)

        self.draw_label("17x17, 60 mines")

    def decorate(self):
        ' ' 'Create start window' ' '
        self.master.title("Minesweeper")

        self.master.geometry("1200x1000")

        self.master.configure(bg="lightgreen")

        label2 = tk.Label(self.master, bg="lightgreen",
                          text="Welcome to Minesweeper!")
        label2.pack()

        start = tk.Button(self.master, text="Start the Game!",
                          command=lambda: self.choose_difficulty()) # pylint: disable=unnecessary-lambda
        # Koodi ei toimi ilman lambdaa
        start.pack(pady=5)

        self.master.mainloop()
