from tkinter import Tk, Canvas

class Window(Canvas):
	def __init__(self, width=500, height=500):
		self.width = width
		self.height = height

	def open(self):
		tk = Tk()
		w = Canvas(tk, width=self.width, height=self.height)
		w.pack()
