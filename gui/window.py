# coding: utf-8
import sys
# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED
else:
    from tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED

BTN_CONFIG = {
    "activebackground": "#6272A4",
    "background": "#44475A",
    "bd": 0,
    "foreground": "#FFFFFF",
    "activeforeground": "#FFFFFF",
    "font": "Bold",
    "relief": SUNKEN
}


class Window:
    def __init__(self, title="PUC-SP", width=500, height=500, background="#ffffff"):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
        self.root = Tk()
        self.root.title(self.title)
        frame = Frame(width=150, height=self.height, bg="#282A36", borderwidth=2)
        frame.pack(side=LEFT)

        self.point_btn = Button(self.root, BTN_CONFIG, text="Ponto")
        self.line_btn = Button(self.root, BTN_CONFIG, text="Reta")
        self.circle_btn = Button(self.root, BTN_CONFIG, text="Círculo")
        self.rectangle_btn = Button(self.root, BTN_CONFIG, text="Retângulo")
        self.undo_btn = Button(self.root, BTN_CONFIG, text="Desfazer", state=DISABLED)
        self.redo_btn = Button(self.root, BTN_CONFIG, text="Refazer", state=DISABLED)

        self.point_btn.place(height=25, width=130, x=10, y=10)
        self.line_btn.place(height=25, width=130, x=10, y=45)
        self.circle_btn.place(height=25, width=130, x=10, y=80)
        self.rectangle_btn.place(height=25, width=130, x=10, y=115)
        self.undo_btn.place(height=25, width=130, x=10, y=150)
        self.redo_btn.place(height=25, width=130, x=10, y=185)

        self.canvas = Canvas(self.root, width=self.width-150, height=self.height, bg=self.background)

    def open(self):
        try:
            return self.canvas.pack(side=RIGHT)
        except Exception as e:
            print("Exception in Window.open: ", e)

    def mainloop(self):
        try:
            self.open()
            mainloop()
            return False
        except Exception as e:
            print('mainloop: ', e)
