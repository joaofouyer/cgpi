from tkinter import Tk, Canvas, mainloop


class Window():
    def __init__(self, title="PUC-SP", width=500, height=500, background="#ffffff"):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
        master = Tk()
        master.title(self.title)
        self.canvas = Canvas(master, width=self.width, height=self.height, bg=self.background)
        self.canvas.pack()

    def open(self):
        try:
            return self.canvas.pack()
        except Exception as e:
            print("Exception in Window.open: ", e)

    def mainloop(self):
        try:
            self.open()
            mainloop()
            return False
        except Exception as e:
            print('mainloop: ', e)
