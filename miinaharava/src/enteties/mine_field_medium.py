import tkinter as tk
import time
from enteties.field import Field
from enteties.filed_start import FieldStart


class MineFieldMedium:
    """ Luokka, joka luo pelin kentän ja vastaa sen tilasta"""

    def __init__(self, master, width, height, image_size, flags_count, parent):

        """ Luokkan konstruktori
        Args:
            master : Tkinterin pääikkuna
            width : Kentän leveys
            height : Kentän korkeus
            image_size : Taustakuvan koko
            flags_count : Lippujen määrä
            parent: Vanhempi luokka, josta kutsutaan tätä luokkaa
        """
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
        """  Tarkistetaan onko kenttä lippu ja muutetaan 
        käytössä olevien lippujen määrää
        Args:
            x : Kentän x-koordinaatti
            y : Kentän y-koordinaatti

        """
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
        """Tarkistetaan, että onko avatun kentän vieressä miinoja ja avataan sitten viereiset kentät
        Args:
            x : Kentän x-koordinaatti
            y : Kentän y-koordinaatti
        """
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
        """Tarkistetaan, että onko peli voitettu

        Args:
            count : Avattujen kenttien määrä
        """
        if count == self.width * self.height - len(self.mines):
            print("You won!")
            self.game_goig = False
            label = tk.Label(self.master, bg="lightgrey",
                             text="You won!", font=("Arial", 20))
            label.place(relx=0.5, rely=0.5, anchor='center')
            time.sleep(2)
            self.parent.choose_difficulty()

    def chekc_loose(self, x, y):
        """Tarkistetaan, että onko peli hävitty
        Args:
            x : Kentän x-koordinaatti
            y : Kentän y-koordinaatti
        """
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
        """ Pelin tilan tarkistus """

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
        """Lippujen määrän piirtäminen
        Args:
            being : Onko lipujen määrä jo piirretty (True) vai ei (False)
        """

        if being is False:
            # Genoroitu alkaa
            self.flag_label = tk.Label(self.master, text=f"Flags: {self.flags_count}", font=("Arial", 14))
            self.flag_label.pack(pady=(5, 0))
            # Genoroitu päättyy
        else:
            self.flag_label.config(text=f"Flags: {self.flags_count}")
            self.flag_label.update_idletasks()

    def create_field(self):
        """Kentän ja alueiden luominen"""

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

        self.field_start.start(self.game_status)
