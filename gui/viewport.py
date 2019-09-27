from tkinter import Canvas, Tk


class Viewport:
    def __init__(self, root, width, height, background="#ffffff"):
        self.root = root
        self.width = width
        self.height = height
        self.background = background
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)

    def reduce_y(y):
        try:
            small_y = (y * 150)/650
            return small_y
        except Exception as e:
            print("Failed to reduce y:", e)

    def reduce_x(x):
        try:
            small_x = (x * 150) / 750
            return small_x
        except Exception as e:
            print("Failed to reduce x:", e)