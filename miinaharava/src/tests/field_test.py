import unittest
import tkinter as tk
from enteties.field import Field

class TestDecorator(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = tk.Tk()
        self.wolf = Field(self.root,8,8)
        self.wolf.draw_field()

    def test_field_values(self):
        self.assertEqual(self.wolf.master, self.root)
        self.assertEqual(self.wolf.x, 8)
        self.assertEqual(self.wolf.y, 8)

    def test_on_click_not_mine(self):
        self.wolf.on_click()
        self.assertTrue(self.wolf.is_opened)
        self.assertFalse(self.wolf.is_flagged)
        self.assertEqual(self.wolf.button.bg, "lightgreen")
        self.assertEqual(self.wolf.on_click(),None)

    # def test_on_click_is_mine(self):
    #     self.wolf.is_mine = True
    #     self.wolf.on_click()
    #     self.assertTrue(self.wolf.is_opened)

    # def test_on_right_click(self):
    #     self.wolf.on_right_click(None)
        # self.assertTrue(self.wolf.is_flagged)
        # self.assertEqual(self.wolf.button.image, None)

