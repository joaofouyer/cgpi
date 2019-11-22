# coding: utf-8
from PIL import Image, ImageTk
import sys

if sys.version_info[0] < 3:
    from Tkinter import Label
else:
    from tkinter import Label


class Photo:
    def __init__(self, filename, filter=None, image=None):
        self.filename = filename
        self.filter = filter
        if image:
            self.image = image
        else:
            self.image = Image.open(self.filename)
        self.photo_image = ImageTk.PhotoImage(self.image)

    def display(self, panel):
        try:
            if panel:
                panel.destroy()
            panel = Label(image=self.photo_image)
            panel.image = self.photo_image
            panel.pack()
            return panel
        except Exception as e:
            print("Exception on display Photo: {} {}".format(type(e), e))
            raise e