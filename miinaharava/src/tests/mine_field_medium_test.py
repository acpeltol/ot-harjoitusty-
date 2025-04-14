import unittest
import tkinter as tk
from enteties.mine_field_medium import MineFieldMedium
from enteties.field import Field


class TestMineFieldMedium(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = tk.Tk()
        self.wolf = MineFieldMedium(self.root)

    def test_mine_field_easy(self):
        self.assertEqual(self.wolf.width, 14)
        self.assertEqual(self.wolf.height, 14)
        self.assertEqual(len(self.wolf.field), 14)
        self.assertEqual(len(self.wolf.field[0]), 14)
        self.assertEqual(self.wolf.flags_count, 40)

    def test_create_field(self):
        self.wolf.create_field()
        self.assertEqual(len(self.wolf.field), 14)
        self.assertEqual(len(self.wolf.field[0]), 14)
        self.assertTrue(isinstance(self.wolf.field[0][0], Field))
