import unittest
import tkinter as tk
from enteties.mine_field_fasy import MineFieldEasy
from enteties.field import Field

class TestMineFieldEasy(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = tk.Tk()
        self.wolf = MineFieldEasy(self.root)

    def test_mine_field_easy(self):
        self.assertEqual(self.wolf.width, 8)
        self.assertEqual(self.wolf.height, 8)
        self.assertEqual(len(self.wolf.field), 8)
        self.assertEqual(len(self.wolf.field[0]), 8)
        self.assertEqual(self.wolf.flags_count, 10)
    
    def test_create_field(self):
        self.wolf.create_field()
        self.assertEqual(len(self.wolf.field), 8)
        self.assertEqual(len(self.wolf.field[0]), 8)
        self.assertTrue(isinstance(self.wolf.field[0][0], Field))
        