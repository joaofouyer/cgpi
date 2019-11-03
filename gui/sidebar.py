import sys

if sys.version_info[0] < 3:
    from Tkinter import Frame, LEFT
else:
    from tkinter import Frame, LEFT


class Sidebar:
    def __init__(self, height, background="#E5E8E8", borderwidth=2):
        self.frame = Frame(width=150, height=height, bg=background, borderwidth=borderwidth)
        self.frame.pack(side=LEFT)
