import unittest
import tkinter as tk
from unittest.mock import patch, MagicMock
from enteties.field import Field
from enteties.mine_field_medium import MineFieldMedium
from tk_deciratir import Tkdecorator


class TestDecorator(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.master = tk.Tk()
        self.tkDec = Tkdecorator(self.master)
        self.father_wolf = MineFieldMedium(self.master, 8, 8, 100,10, self.tkDec)
        self.wolf = Field(self.master, 8, 8, 50, self.father_wolf)
        self.wolf.draw_field()

    def test_field_values(self):
        self.assertEqual(self.wolf.master, self.master)
        self.assertEqual(self.wolf.x, 8)
        self.assertEqual(self.wolf.y, 8)

    def test_on_click_not_mine(self):
        self.wolf.on_click()
        self.assertTrue(self.wolf.is_opened)
        self.assertFalse(self.wolf.is_flagged)
        self.assertEqual(self.wolf.button.bg, "lightgreen")
        self.assertEqual(self.wolf.on_click(), None)

    def test_on_click_is_mine(self):
        self.wolf.check_sound = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.is_mine = True
        self.wolf.on_click()
        self.wolf.check_sound.assert_called_once()
        self.wolf.draw_button.assert_called_once()
        self.assertTrue(self.wolf.is_opened)

    def test_on_click_is_not_mine(self):
        self.wolf.check_sound = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.mines_near_count = 1
        self.wolf.on_click()
        self.wolf.check_sound.assert_called_once()
        self.wolf.draw_button.assert_called_once()
        self.assertTrue(self.wolf.is_opened)

    def test_on_right_click_is_opened(self):
        self.wolf.check_sound = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.is_opened = True
        # self.wolf.on_right_click()
        # self.wolf.check_sound.assert_called_once()
        # self.wolf.draw_button.assert_called_once()
        self.assertEqual(self.wolf.on_right_click("MouseButton-3"), None)

    def test_on_right_click_is_not_flagged(self):
        self.wolf.check_sound = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.on_right_click("MouseButton-3")
        self.wolf.check_sound.assert_called_once()
        self.assertTrue(self.wolf.is_flagged)
        self.wolf.draw_button.assert_called_once()

    def test_on_right_click_is_flagged(self):
        self.wolf.check_sound = MagicMock()
        self.wolf.draw_button = MagicMock()
        self.wolf.is_flagged = True
        self.wolf.on_right_click("MouseButton-3")
        self.wolf.check_sound.assert_called_once()
        self.assertFalse(self.wolf.is_flagged)
        # self.wolf.draw_button.assert_called_once()


    # def test_on_right_click(self):
    #     self.wolf.on_right_click(None)
        # self.assertTrue(self.wolf.is_flagged)
        # self.assertEqual(self.wolf.button.image, None)

    
