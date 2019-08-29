# coding: utf-8
import sys
# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, mainloop
else:
    from tkinter import Tk, Canvas, mainloop

class Window:

    def __init__(self, title="PUC-SP", width=500, height=500, background="#ffffff"):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
        self.root = Tk()
        self.root.title(self.title)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)

    def open(self):
        try:
            return self.canvas.pack()
        except Exception as e:
            print("Exception in Window.open: ", e)

    def mainloop(self):
        try:
            self.open()
            mainloop()
            return False
        except Exception as e:
            print('mainloop: ', e)
