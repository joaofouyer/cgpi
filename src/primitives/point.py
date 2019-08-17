from src.primitives.coordinate import Coordinate


class Point():
    def __init__(self, window=None, coordinate=Coordinate(), size=2, color="#000000"):
        try:
            x, y = coordinate.get_coordinate()
            self.window = window
            self.x = x
            self.y = y
            self.size = size
            self.color = color

        except Exception as e:
            print("Exception in Point's init: ", e)

    def draw(self):
        try:
            self.window.canvas.create_rectangle( (self.x, self.y) * self.size, fill=self.color, outline=self.color)
            return False
        except Exception as e:
            print("Exception in Point.draw(): ", e)
            return True

    def valid_coordinate(self):
        try:
            if self.x < 0 or self.window.width < self.x:
                #    Adicionar tratamento quando o valor de x for inválido.
                return True
            if self.y < 0 or self.window.height < self.y:
                #    Adicionar tratamento quando o valor de y for inválido.
                return True
        except Exception as e:
            print("Exception in Point. ", e)