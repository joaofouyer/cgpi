# coding: utf-8
import sys
import os
from PIL import ImageFilter
from image_processor.histogram import Histogram
from .action import Action
from .photo import Photo

# Importante para garantir que funcione em python2 e em python3.
if sys.version_info[0] < 3:
    from Tkinter import Tk, mainloop, Button, CENTER, filedialog, Frame, TOP, StringVar, OptionMenu, RIGHT
else:
    from tkinter import Tk, mainloop, Button, CENTER, filedialog, Frame, TOP, StringVar, OptionMenu, RIGHT

BTN_CONFIG = {
    "border": "0",
    "activebackground": "#282A36",
    "background": "#282A36",
    "highlightbackground": "#282A36",
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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Window:
    def __init__(self, title="Processamento de Imagem", width=1000, height=700, background="#282A36"):
        try:
            self.root = Tk()
            self.root.title(title)
            self.root.configure(background=background, width=width, height=height)
            self.root.resizable(width=False, height=False)
            self.root.geometry('%dx%d+%d+%d' % (width, height, 0, 0))
            self.height = height
            self.background = background
            self.menu = Frame(self.root, width=width, height=70, bg=background, borderwidth=1)
            self.menu.pack(side=TOP)

            # self.panel = Frame(self.root, width=width, height=630, bg=background, borderwidth=0)
            # self.panel.pack(side=BOTTOM)

            self.sidebar = Frame(self.root, width=50, height=100, bg=self.background, borderwidth=1)
            self.sidebar.pack(side=RIGHT)

            self.panel = None
            self.actions = Action()

            filter_options = ["Monocromático", "Escala de Cinza", "Blur", "Daltônico"]
            var = StringVar(self.menu)
            var.set("Filtros")

            self.load_image_btn = Button(self.menu, BTN_CONFIG,  text="Carregar", command=self.load_file)
            self.save_image_btn = Button(self.menu, BTN_CONFIG,  text="Salvar", command=None)
            self.undo_btn = Button(self.menu, BTN_CONFIG,  text="Desfazer", command=self.undo)
            self.redo_btn = Button(self.menu, BTN_CONFIG,  text="Refazer", command=self.redo)
            self.histogram_btn = Button(self.menu, BTN_CONFIG,  text="Histograma", command=self.histogram)
            self.filters_btn = OptionMenu(self.menu, var, *filter_options, command=self.apply_filter)
            self.filters_btn.config(
                bg="#282A36", border=0, activebackground="#282A36", highlightbackground="#282A36",
                bd=0, foreground="#FFFFFF", activeforeground="#FFFFFF"
            )
            self.filters_btn["menu"].config(
                bg="#282A36", border=0, activebackground="#282A36",
                bd=0, foreground="#FFFFFF", activeforeground="#FFFFFF"
            )

            self.load_image_btn.place(height=20, width=60, x=5, y=5)
            self.save_image_btn.place(height=20, width=60, x=70, y=5)
            self.undo_btn.place(height=20, width=60, x=140, y=5)
            self.redo_btn.place(height=20, width=70, x=210, y=5)
            self.histogram_btn.place(height=20, width=80, x=290, y=5)
            self.filters_btn.place(height=20, width=90, x=370, y=5)

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

    def display_image(self, filename):
        try:
            image = Photo(filename=filename)
            self.panel = image.display(panel=self.panel)
            self.actions.push(image=image)
        except Exception as e:
            print("Exception on display_image: {} {}".format(type(e), e))
            raise e

    def load_file(self):
        try:
            filename = filedialog.askopenfilename(
                initialdir=BASE_DIR, title="Selecione a imagem.",
                filetypes=(("Arquivos JPEG, PNG, GIF", "*.jpeg *.jpg *.png *.gif"), ("todos os arquivos", "*.*"))
            )
            if filename:
                self.display_image(filename=filename)
            return False
        except Exception as e:
            print("Exception on load_file: {} {}".format(type(e), e))
            raise e

    def apply_filter(self, value):
        try:
            options = {
                "Monocromático": self.monochromatic,
                "Escala de Cinza": self.bw,
                "Blur": self.gaussian,
                "Daltônico": self.daltonic
            }
            return options[value]()
        except Exception as e:
            print("Exception on window apply filter: {} {}".format(type(e), e))
            raise e

    def monochromatic(self):
        try:
            mono = self.actions.last()
            thresh = 100
            fn = lambda x: 255 if x > thresh else 0
            r = mono.image.convert('L').point(fn, mode='1')
            mono = Photo(filename=mono.filename, filter="monocromatico", image=r)
            self.actions.push(image=mono)
            self.panel = mono.display(panel=self.panel)
        except Exception as e:
            print("Exception on monochromatic: {} {}".format(type(e), e))
            raise e

    def bw(self):
        try:
            photo = self.actions.last()
            bw = photo.image.convert('LA')
            bw = Photo(filename=photo.filename, filter="bw", image=bw)
            self.panel = bw.display(panel=self.panel)
            self.actions.push(image=bw)
        except Exception as e:
            print("Exception on bw: {} {}".format(type(e), e))
            raise e

    def gaussian(self):
        try:
            photo = self.actions.last()
            blur = photo.image
            blur = blur.filter(ImageFilter.BLUR)
            blur = Photo(filename=photo.filename, filter="blur", image=blur)
            self.panel = blur.display(panel=self.panel)
            self.actions.push(image=blur)
        except Exception as e:
            print("Exception on gaussian: {} {}".format(type(e), e))
            raise e

    def daltonic(self):
        try:
            pass
        except Exception as e:
            print("Exception on daltonic: {} {}".format(type(e), e))
            raise e

    def undo(self):
        try:
            image = self.actions.undo()
            if image:
                self.panel = image.display(panel=self.panel)

        except Exception as e:
            print("Exception on undo: {} {}".format(type(e), e))
            raise e

    def redo(self):
        try:
            image = self.actions.redo()
            if image:
                self.panel = image.display(panel=self.panel)

        except Exception as e:
            print("Exception on redo: {} {}".format(type(e), e))
            raise e

    def histogram(self):
        try:
            img = self.actions.last()
            histogram = Histogram(photo=img, root=self.sidebar)

        except Exception as e:
            print("Exception on histogram: {} {}".format(type(e), e))
            raise e
