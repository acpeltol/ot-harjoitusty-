import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from enteties.filed_start import FieldStart
from enteties.mine_field_medium import MineFieldMedium
from enteties.field import Field
import tk_deciratir


class TestDecorator(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.master = tk.Tk()
        self.tkDec = tk_deciratir.Tkdecorator(self.master)
        self.father_wolf = MineFieldMedium(self.master, 8, 8, 100,10, self.tkDec)
        self.wolf = FieldStart(self.father_wolf)

    def test_field_values(self):
        self.assertEqual(self.father_wolf, self.wolf.parent)

    def test_set_mines(self):

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)


        for y in range(self.father_wolf.height):
            for x in range(self.father_wolf.width):
                self.father_wolf.field[y][x] = Field(self.grid_frame, x, y, 100, self.father_wolf)
                self.father_wolf.field[y][x].draw_field()

        self.father_wolf.field[2][2].is_opened = True

        self.wolf.banned.add((2,2))

        self.wolf.set_mines()

        boolen = (2,2) in self.wolf.banned

        print(self.wolf.banned)

        self.assertEqual(True, boolen)

        self.assertEqual(len(self.father_wolf.mines), 10)

        boolen2 = (2,2) not in self.father_wolf.mines

        self.assertEqual(True, boolen2)

    def test_check_mines(self):

        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack(fill=tk.BOTH, expand=True)


        for y in range(self.father_wolf.height):
            for x in range(self.father_wolf.width):
                self.father_wolf.field[y][x] = Field(self.grid_frame, x, y, 100, self.father_wolf)
                self.father_wolf.field[y][x].draw_field()

        self.father_wolf.field[2][2].is_opened = True

        self.wolf.banned.add((2,2))

        self.wolf.set_mines()

        self.wolf.set_mines_near()

        one = next(iter(self.father_wolf.mines))

        print(self.father_wolf.mines)

        print(one)

        x = one[1]
        y = one[0]
        print((x,y))
        boolen = self.father_wolf.field[x][y].is_mine

        self.assertEqual(boolen, True)