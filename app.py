from window import Window
from primitives.coordinate import Coordinate
from primitives.point import Point
from animation import Animation

def main():
    try:
        w = Window(title="Testando Pontos Animados", width=640, height=480, background="#000000")
        a = Animation(window=w)
        for i in range(50, 450):
            c = Coordinate(x=i, y=i)
            p = Point(window=w, coordinate=c, color="#ffffff")
            a.append_frame(p)
        a.animate()
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True

main()
