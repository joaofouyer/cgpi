from window import Window
from coordinates import Coordinates
from tkinter import Tk, Canvas


class Pixel():
	def draw(window, coordinates=Coordinates(), color='black'):
		x, y = coordinates.get_coordinates()
		tk = Tk()
		window = Canvas(tk, width=500, height=500)
		window.pack()
		if x < 0 or window.width < x:
			#	Adicionar tratamento quando o valor de x for inválido.
			return True
		if y < 0 or window.height <  y:
			#	Adicionar tratamento quando o valor de y for inválido.
			return True 

		window.create_rectangle( (x, y) * 2 )
