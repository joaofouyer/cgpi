# coding: utf-8
import sys
from canvas.gui.window import Window as CanvasWindow
from canvas.structures.action import Action
from image_processor.window import Window as ImageWindow

# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, mainloop, Button, Label, CENTER
else:
    from tkinter import Tk, mainloop, Button, Label, CENTER

BTN_CONFIG = {
    "border": "0",
    "activebackground": "#6272A4",
    "background": "#44475A",
    "bd": "0",
    "borderwidth": 0,
    "foreground": "#ffffff",
    "activeforeground": "#ffffff",
    "font": "Bold"
}

LABEL_CONFIG = {
    "border": "0",
    "activebackground": "#282A36",
    "background": "#282A36",
    "font": "Bold",
    "activeforeground": "#FFFFFF",
    "foreground": "#FFFFFF",
    "anchor": CENTER,
    "borderwidth": 0
}


class MainWindow:
    def __init__(self, title="CGPI", width=400, height=100, background="#282A36"):
        try:
            self.root = Tk()
            self.root.title(title)
            self.root.configure(background=background, width=width, height=height)
            self.root.resizable(width=False, height=False)
            self.canvas_btn = Button(self.root, BTN_CONFIG,  text="Canvas", command=self.open_canvas)
            self.img_btn = Button(self.root, BTN_CONFIG,  text="Imagem", command=self.open_image)
            self.canvas_btn.place(height=40, width=90, x=70, y=50)
            self.img_btn.place(height=40, width=90, x=240, y=50)
            self.w = Label(self.root, LABEL_CONFIG, text="Escolha a aplicação que deseja abrir")
            self.w.config(font=("Courier", 16))
            self.w.place(x=20, y=5)
        except Exception as e:
            print("Exception on window constructor: {} {}".format(type(e), e))
            raise e

    @staticmethod
    def mainloop():
        try:
            mainloop()
            return False
        except Exception as e:
            print("Exception on mainloop: {} {}".format(type(e), e))
            raise e

    def open_canvas(self):
        try:
            self.root.destroy()
            w = CanvasWindow(title="PUC-SP", width=600, height=600, background="white", actions=Action())
            w.mainloop()
            return False
        except Exception as e:
            print("Exception on open_canvas: {} {}".format(type(e), e))
            raise e

    def open_image(self):
        try:
            self.root.destroy()
            w = ImageWindow()
            w.mainloop()
            return False
        except Exception as e:
            print("Exception on open_image: {} {}".format(type(e), e))
            raise e
