# coding: utf-8
import sys
# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, Toplevel, YES, BOTH
else:
    from tkinter import Tk, Canvas, Toplevel, YES, BOTH


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
            self.top_margin = min_y
            self.left_margin = min_x
            self.background = background
            top_level = Toplevel(
                self.root,
                height=self.height,
                width=self.width,
                background=self.background
            )
            self.canvas = Canvas(top_level, width=self.width, height=self.height, bg=self.background)
            self.canvas.pack(expand=YES, fill=BOTH)
        except Exception as e:
            print("Exception on clipping constructor: {} {}".format(type(e), e))
            raise e