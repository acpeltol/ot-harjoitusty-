import unittest
import tkinter as tk
from tkDeciratir import Tkdecorator

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        print("Set up goes here")

    def test_decorator(self):
        root = tk.Tk()
        wolf = Tkdecorator(root)
        self.assertEqual(wolf.master, root)