from window import Window
from primitives.coordinate import Coordinate
from primitives.point import Point
from primitives.line import Line


def main():
    try:
        w = Window(title="Testando Pontos Animados", width=640, height=480, background="#000000")
        coordinate_p1 = Coordinate(x=50, y=300)
        p1 = Point(window=w, coordinate=coordinate_p1)
        coordinate_p2 = Coordinate(x=450, y=300)
        p2 = Point(window=w, coordinate=coordinate_p2)
        l = Line(p1=p1, p2=p2, color="#ffffff", thickness=2)
        l.draw(w=w, animation=True)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True


main()
