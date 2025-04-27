import unittest
import tkinter as tk
from enteties.mine_field_medium import MineFieldMedium
from unittest.mock import patch, MagicMock
from enteties.field import Field


class TestMineFieldMedium(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")
        self.root = tk.Tk()
        self.wolf = MineFieldMedium(self.root, 14, 14, 60, 40)
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

    # def test_after_field_create(self):
    #     self.wolf.game_status = MagicMock()
    #     self.wolf.after_field_created()
    #     self.wolf.game_status.assert_called_once()

    def test_check_flagged(self):
        self.wolf.field[0][0].is_flagged = True
        self.wolf.check_flagged(0, 0)
        self.assertEqual(self.wolf.check_flagged(0, 0), None)

        self.assertEqual(self.wolf.flags_count, 39)

        self.wolf.field[0][0].is_flagged = False
        self.wolf.check_flagged(0, 0)
        self.assertEqual(self.wolf.flags_count, 40)
        self.assertEqual(self.wolf.check_flagged(0, 0), None)

    
