# coding: utf-8
import sys
# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Canvas
else:
    from tkinter import Canvas


class Viewport:
    def __init__(self, root, width=200, height=200, background="#ffffff"):
        self.root = root
        self.width = width
        self.height = height
        self.background = background
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)

    def reduce(self, x, y, window):
        try:
            small_y = (y * self.height) / window.height
            small_x = (x * self.width) / window.canvas_width
            return small_x, small_y
        except Exception as e:
            print("Exception on reduce: ", e)
            return True
