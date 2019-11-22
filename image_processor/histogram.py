from tkinter import TOP, X
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
from matplotlib.backend_bases import NavigationToolbar2
from matplotlib.figure import Figure
import numpy as np



class Histogram:
    def __init__(self, photo, root):
        try:
            self.photo = photo
            self.generate(root)
        except Exception as e:
            print("Histogram: ", type(e), e)
            raise e

    def plot(self, l, root):
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
