# coding: utf-8
from gui.window import Window
from structures.action import Action
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if sys.version_info[0] < 3:
    from Tkinter import PhotoImage
else:
    from tkinter import PhotoImage

def main():
    try:
        w = Window(title="PUC-SP", width=600, height=600, background="white", actions=Action())
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True

main()
