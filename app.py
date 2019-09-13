# coding: utf-8
from gui.window import Window
from primitives.coordinate import Coordinate
from primitives.circle_graph import CircleGraph


def main():
    try:
        w = Window(title="Testando Desfazer Ações", width=640, height=480, background="white")
        cc = CircleGraph(center=Coordinate(x=50, y=50), radius=50, color="#000000", thickness=2)
        cc.draw(window=w)
        w.mainloop()
        return False

    except Exception as e:
        print("Exception on main(): ", e)
        return True
    
main()