from tkinter import TOP, X
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.figure import Figure


class Histogram:
    def __init__(self, photo, root):
        try:
            self.photo = photo
            self.generate(root)
        except Exception as e:
            print("Histogram: ", type(e), e)
            raise e

    @staticmethod
    def plot(l, root):
        fig = Figure(figsize=(5, 4), dpi=50)
        fig.add_subplot(111).plot(l)

        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=X, side=TOP)

    def generate(self, root):
        try:
            histogram = self.photo.image.histogram()
            r = histogram[0:256]
            g = histogram[256:512]
            b = histogram[512:768]
            self.plot(r, root)
            self.plot(g, root)
            self.plot(b, root)

        except Exception as e:
            print("generate: ", type(e), e)
            raise e
