from tkinter import Canvas, Tk


class Viewport:
    def __init__(self, title="Viewport", width=200, height=200, background="#ffffff"):

        self.title = title
        self.width = width
        self.height = height
        self.background = background
        self.root = Tk()
        self.root.title(self.title)
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)

        self.root.mainloop()

