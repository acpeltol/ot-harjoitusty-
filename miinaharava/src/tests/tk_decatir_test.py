import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from tk_deciratir import Tkdecorator
from enteties.mine_field_medium import MineFieldMedium


class TestDecorator(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = tk.Tk()
        self.wolf = Tkdecorator(self.root)
        self.wolf.clear_window = MagicMock()
        #self.wolf.master = MagicMock()

    def test_decorator(self):
        self.assertEqual(self.wolf.master, self.root)

    def test_choos_difficulty(self):
        self.wolf.clear_window = MagicMock()
        self.wolf.draw_label = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.master = MagicMock()

        self.wolf.choose_difficulty()

        self.wolf.clear_window.assert_called_once()
        # self.wolf.master.configure.assert_called_with(bg="lightgreen")
        self.wolf.draw_label.assert_any_call("Choose difficulty")
        self.wolf.draw_button.assert_any_call("Easy", 1)
        self.wolf.draw_label.assert_any_call("8x8, 10 mines")
        self.wolf.draw_button.assert_any_call("Medium", 2)
        self.wolf.draw_label.assert_any_call("14x14, 40 mines")
        self.wolf.draw_button.assert_any_call("Hard", 3)
        self.wolf.draw_label.assert_any_call("17x17, 60 mines")







