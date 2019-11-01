# coding: utf-8
import sys
# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, Toplevel
else:
    from tkinter import Tk, Canvas, Toplevel


class Clipping:
    def __init__(self, root, min_x, min_y, max_x, max_y, background="#ffffff"):
        try:
            self.root = root
            if min_x < max_x:
                self.min_x = min_x
                self.max_x = max_x
            else:
                self.min_x = max_x
                self.max_x = min_x
            if min_y < max_y:
                self.min_y = min_y
                self.max_y = max_y
            else:
                self.min_y = max_y
                self.max_y = min_y

            self.width = self.max_x - self.min_x
            self.height = self.max_y - self.min_y
            self.background = background
            self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)
        except Exception as e:
            print("Exception on clipping constructor: {} {}".format(type(e), e))
            raise e

    def open(self):
        try:
            clipping = Toplevel(self.root, height=self.height, width=self.width, background=self.background)
        except Exception as e:
            print("Exception on open_clipping: {} {}".format(type(e), e))
            raise e
