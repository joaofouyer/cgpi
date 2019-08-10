from window import Window
from coordinates import Coordinates
from pixel import Pixel


def main():
	try:
		canvas = Window(width=500, height=500)
		canvas.open()
		c =  Coordinates(x=250, y=250)
		Pixel.draw(window=canvas, coordinates=c)
		return False
	except Exception as e:
		print('main: ', e)
		return True
main()