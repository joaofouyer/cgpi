# coding: utf-8

from main_window import MainWindow
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        w = MainWindow()
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


main()
