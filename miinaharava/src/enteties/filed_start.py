import random as rand
import pygame as pg


class FieldStart:
    ' ' 'Class for handling the start of the game, first click and setting the mines' ' '
    def __init__(self, parent):
        self.parent = parent
        self.width = parent.width
        self.height = parent.height
        self.explosion_count = set()
        self.banned = set()
        self.oppened = None

    def set_mines(self):
        ' ''Placing the mines into fields randoly' ' '
        pos = [(x, y) for x in range(self.width) for y in range(self.height)
               if (x, y) not in self.banned]

        minen = rand.sample(pos, self.parent.flags_count)

        self.parent.mines = set(minen)

        for mine in minen:
            self.parent.field[mine[1]][mine[0]].is_mine = True

    def check_mines_blcok(self, x, y):
        ' ' 'Checking how many mines are near fields' ' '
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (i == 0 and j == 0):
                    continue
                if (y + i < 0 or y + i >= self.height
                        or x + j < 0 or x + j >= self.width):
                    continue
                if self.parent.field[y + i][x + j].is_mine is True:
                    count += 1
        self.parent.field[y][x].mines_near_count = count

    def set_mines_near(self):
        ' ' 'Checking if field is mine, if not then calling mines near function' ' '
        for y in range(self.height):
            for x in range(self.width):
                if self.parent.field[y][x].is_mine is True:
                    continue
                self.check_mines_blcok(x, y)

    def open_fields(self, bage):
        ' ' 'Opening the fields near by of empty field' ' '

        y = bage[1]
        x = bage[0]

        for i in range(-1, 2):
            for j in range(-1, 2):
                # print(f"i: {y + i}, j: {x + j}")
                if (i == 0 and j == 0):
                    continue
                if (y + i < 0 or y + i >= self.height
                        or x + j < 0 or x + j >= self.width):
                    continue
                if (x + j, y + i) in self.explosion_count:
                    continue
                if self.parent.field[y + i][x + j].mines_near_count == 0:
                    self.parent.field[y + i][x + j].on_click(True)
                    self.explosion_count.add((x + j, y + i))
                    self.open_fields((x + j, y + i))
                else:
                    self.parent.field[y + i][x + j].on_click(True)
                    self.explosion_count.add((x + j, y + i))

        return True

    def first_explosion(self):

        self.set_mines()
        self.set_mines_near()

        self.open_fields(self.oppened)

    def start(self, finnish):

        for y in range(self.height):
            for x in range(self.width):
                if self.parent.field[y][x].is_opened is True:

                    pg.mixer.init()
                    sound = pg.mixer.Sound("src/audio/minesweeper_dig_once.wav")
                    sound.play()

                    self.banned.add((x, y))
                    self.banned.add((x + 1, y))
                    self.banned.add((x - 1, y))
                    self.banned.add((x, y + 1))
                    self.banned.add((x, y - 1))
                    self.banned.add((x + 1, y + 1))
                    self.banned.add((x - 1, y - 1))
                    self.banned.add((x + 1, y - 1))
                    self.banned.add((x - 1, y + 1))
                    self.oppened = (x, y)
                    self.first_explosion()

                    if finnish:
                        finnish()

                    return True

        self.parent.master.after(100, lambda: self.start(finnish))
