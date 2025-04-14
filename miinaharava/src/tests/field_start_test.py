import unittest
import tkinter as tk
from enteties.filed_start import FieldStart
from enteties.mine_field_fasy import MineFieldEasy
from enteties.field import Field


class TestDecorator(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.master = tk.Tk()
        self.father_wolf = MineFieldEasy(self.master)
        self.wolf = FieldStart(self.father_wolf)

    def test_field_values(self):
        self.assertEqual(self.father_wolf, self.wolf.parent)

    # def test_ignore_values(self):

    #     self.grid_frame = tk.Frame(self.master)
    #     self.grid_frame.pack(fill=tk.BOTH, expand=True)

        
    #     for y in range(self.father_wolf.height):
    #         for x in range(self.father_wolf.width):
    #             self.father_wolf.field[y][x] = Field(self.grid_frame, x, y, 100)
    #             self.father_wolf.field[y][x].draw_field()

    #     self.father_wolf.field[2][2].on_click()

    #     self.wolf.start(None)

    #     boolen = (2,2) in self.wolf.banned

    #     self.assertEqual(True, boolen)

