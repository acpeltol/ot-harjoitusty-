import unittest
import tkinter as tk
from enteties.mine_field_medium import MineFieldMedium
from unittest.mock import patch, MagicMock
from enteties.field import Field
import tk_deciratir


class TestMineFieldMedium(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.master = tk.Tk()
        self.tkDec = tk_deciratir.Tkdecorator(self.master)
        self.wolf = MineFieldMedium(self.master, 14, 14, 60,40, self.tkDec)
        self.wolf.create_field()

    def test_mine_field_easy(self):
        self.assertEqual(self.wolf.width, 14)
        self.assertEqual(self.wolf.height, 14)
        self.assertEqual(len(self.wolf.field), 14)
        self.assertEqual(len(self.wolf.field[0]), 14)
        self.assertEqual(self.wolf.flags_count, 40)

    def test_create_field(self):
        self.assertEqual(len(self.wolf.field), 14)
        self.assertEqual(len(self.wolf.field[0]), 14)
        self.assertTrue(isinstance(self.wolf.field[0][0], Field))

    def test_check_flagged(self):
        self.wolf.field[0][0].is_flagged = True
        self.wolf.check_flagged(0, 0)
        self.assertEqual(self.wolf.check_flagged(0, 0), None)

        self.assertEqual(self.wolf.flags_count, 39)

        self.wolf.field[0][0].is_flagged = False
        self.wolf.check_flagged(0, 0)
        self.assertEqual(self.wolf.flags_count, 40)
        self.assertEqual(self.wolf.check_flagged(0, 0), None)

    def test_chekc_if_empty(self):
        self.wolf.field_start.open_fields = MagicMock()
        self.wolf.field[0][0].is_opened = False
        self.assertEqual(self.wolf.check_if_empty_field(0, 0), None)

        self.wolf.field[4][4].is_opened = True
        self.wolf.field[4][4].mines_near_count = 1
        self.assertEqual(self.wolf.check_if_empty_field(4, 4), None)

        self.wolf.field[1][1].is_opened = True
        self.wolf.field_start.explosion_count.add((1, 1))
        self.assertEqual(self.wolf.check_if_empty_field(1, 1), None)
        

        self.wolf.field[2][2].is_opened = True
        self.wolf.field[2][2].mines_near_count = 0
        self.wolf.field[2][2].is_mine = True
        self.assertEqual(self.wolf.check_if_empty_field(2, 2), None)

        self.wolf.field[3][3].is_opened = True
        self.wolf.field[3][3].mines_near_count = 0
        self.wolf.field[3][3].is_mine = False

        self.wolf.check_if_empty_field(3, 3)

        self.wolf.field_start.open_fields.assert_called_once()

    # def test_game_status(self):
    #     self.wolf.check_vicotry = MagicMock()
    #     self.wolf.chekc_loose = MagicMock()
    #     self.wolf.check_if_empty_field = MagicMock()
    #     self.wolf.check_flagged = MagicMock()
    #     self.wolf.field[0][0].is_opened = True

    #     self.wolf.game_status()
    #     self.wolf.check_flagged.assert_any_call()
    #     self.wolf.chekc_loose.assert_any_call()
    #     self.wolf.check_if_empty_field.assert_any_call()
    #     self.wolf.check_vicotry.assert_any_call()



    
