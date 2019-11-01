# coding: utf-8
from structures.action import Action
from structures.import_file import import_json
from structures.export_file import export_json
from primitives.point_graph import PointGraph
from primitives.circle_graph import CircleGraph
from primitives.line_graph import LineGraph
from primitives.rectangle_graph import RectangleGraph
from primitives.polygon_graph import PolygonGraph
from gui.viewport import Viewport
import sys
import os

# Importante para garantir que funcione em python2 e em python3.

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED, Tkinter, Tkconstants,\
        tkFileDialog
else:
    from tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED, filedialog

BTN_CONFIG = {
    "activebackground": "#6272A4",
    "background": "#44475A",
    "bd": 0,
    "foreground": "#FFFFFF",
    "activeforeground": "#FFFFFF",
    "font": "Bold",
    "relief": SUNKEN
}


class Window:
    def __init__(self, title="PUC-SP", width=500, height=500, background="#ffffff", actions=Action()):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
        self.root = Tk()
        self.root.title(self.title)
        self.actions = actions
        self.root.resizable(width=False, height=False)
        sidebar = Frame(width=150, height=self.height, bg="#282A36", borderwidth=2)
        sidebar.pack(side=LEFT)

        self.line_btn = Button(self.root, BTN_CONFIG, text="Reta", command=self.draw_line)
        self.circle_btn = Button(self.root, BTN_CONFIG, text="Círculo", command=self.draw_circle)
        self.rectangle_btn = Button(self.root, BTN_CONFIG, text="Retângulo", command=self.draw_rectangle)
        self.polygon_btn = Button(self.root, BTN_CONFIG, text="Polígono", command=self.draw_polygon)
        self.undo_btn = Button(self.root, BTN_CONFIG, text="Desfazer", state=DISABLED, command=self.undo)
        self.redo_btn = Button(self.root, BTN_CONFIG, text="Refazer", state=DISABLED, command=self.redo)
        self.import_btn = Button(self.root, BTN_CONFIG, text="Importar", state="normal", command=self.import_file)
        self.export_btn = Button(self.root, BTN_CONFIG, text="Exportar", state=DISABLED, command=self.export_file)

        self.line_btn.place(height=20, width=130, x=10, y=10)
        self.circle_btn.place(height=20, width=130, x=10, y=40)
        self.rectangle_btn.place(height=20, width=130, x=10, y=70)
        self.polygon_btn.place(height=20, width=130, x=10, y=100)
        self.undo_btn.place(height=20, width=130, x=10, y=130)
        self.redo_btn.place(height=20, width=130, x=10, y=160)
        self.import_btn.place(height=20, width=130, x=10, y=190)
        self.export_btn.place(height=20, width=130, x=10, y=220)

        self.canvas_width = self.width
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.height, bg=self.background)
        self.viewport = Viewport(
            root=self.root,
            width=140,
            height=(self.height*0.15),
            background=self.background
        )
        self.viewport.canvas.place(x=5, y=(self.height - self.height*0.17))

        self.active_draw_mode = None
        self.canvas.old_coords = None

    def open(self):
        try:
            self.refresh()
            return self.canvas.pack(side=RIGHT)
        except Exception as e:
            print("Exception on open window: {} {}".format(type(e), e))
            raise e

    def mainloop(self):
        try:
            self.open()
            self.canvas.bind('<ButtonPress-1>', self.click_event)
            mainloop()
            return False
        except Exception as e:
            print("Exception on mainloop: {} {}".format(type(e), e))
            raise e

    def update_undo_btn_state(self):
        try:
            if len(self.actions.actions_stack):
                self.undo_btn.config(state="normal")
                self.export_btn.config(state="normal")
            else:
                self.undo_btn.config(state="disabled")
                self.export_btn.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update undo btn state: {} {}".format(type(e), e))
            raise e

    def update_redo_btn_state(self):
        try:
            if len(self.actions.undo_stack):

                self.redo_btn.config(state="normal")
            else:

                self.redo_btn.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update redo btn state: {} {}".format(type(e), e))
            raise e

    def refresh(self):
        try:
            self.update_redo_btn_state()
            self.update_undo_btn_state()
        except Exception as e:
            print("Exception on refresh: {} {}".format(type(e), e))
            raise e

    def undo(self):
        try:
            return self.actions.undo(window=self)
        except Exception as e:
            print("Exception on undo: {} {}".format(type(e), e))
            raise e

    def redo(self):
        try:
            return self.actions.redo(window=self)
        except Exception as e:
            print("Exception on redo: {} {}".format(type(e), e))
            raise e

    def click_event(self, event):
        try:
            point = PointGraph(x=event.x, y=event.y, window=self)
            if self.active_draw_mode == "POINT":
                point.draw(append_action=True)
                self.canvas.old_coords = None
            else:
                if self.canvas.old_coords:
                    p1 = self.canvas.old_coords
                    p2 = point
                    if self.active_draw_mode == "LINE":
                        line = LineGraph(p1=p1, p2=p2)
                        line.draw(window=self, animation=False)
                        self.canvas.old_coords = None
                    elif self.active_draw_mode == "CIRCLE":
                        line = LineGraph(p1=p1, p2=p2)
                        circle = CircleGraph(center=p1, radius=line.length)
                        circle.draw(window=self)
                        self.canvas.old_coords = None
                    elif self.active_draw_mode == "RECTANGLE":
                        rectangle = RectangleGraph(p1=p1, p2=p2)
                        rectangle.draw(window=self)
                        self.canvas.old_coords = None
                    elif self.active_draw_mode == "POLYGON":
                        polygon = self.actions.active_polygon
                        first = polygon.points[0]
                        if first.x - 5 < p2.x < first.x + 5 and first.y - 5 < p2.y < first.y + 5:
                            self.actions.push(polygon)
                            self.canvas.create_rectangle(
                                first.x + 3,
                                first.y + 3,
                                first.x - 3,
                                first.y - 3,
                                outline=self.background
                            )
                            polygon.push(point=first)
                            polygon.draw(window=self, multiple_points=False)
                            polygon.points.pop()
                            self.canvas.old_coords = None

                        else:
                            polygon.push(point=p2)
                            polygon.draw(window=self, multiple_points=False)
                            self.canvas.old_coords = p2
                else:
                    self.canvas.old_coords = point
                    if self.active_draw_mode == "POLYGON":
                        self.actions.active_polygon = PolygonGraph()
                        self.actions.active_polygon.push(point)
                        self.canvas.create_rectangle(point.x+3, point.y+3, point.x-3, point.y-3)

            return False
        except Exception as e:
            print("Exception on click event: {} {}".format(type(e), e))
            raise e

    def draw_point(self):
        try:
            self.active_draw_mode = "POINT"
            self.canvas.old_coords = None
            return False
        except Exception as e:
            print("Exception on draw point: {} {}".format(type(e), e))
            raise e

    def draw_line(self):
        try:
            self.active_draw_mode = "LINE"
            self.canvas.old_coords = None
            return False
        except Exception as e:
            print("Exception on draw line: {} {}".format(type(e), e))
            raise e

    def draw_circle(self):
        try:
            self.active_draw_mode = "CIRCLE"
            self.canvas.old_coords = None
            return False
        except Exception as e:
            print("Exception on draw circle: {} {}".format(type(e), e))
            raise e

    def draw_rectangle(self):
        try:
            self.active_draw_mode = "RECTANGLE"
            self.canvas.old_coords = None
            return False
        except Exception as e:
            print("Exception on draw rectangle: {} {}".format(type(e), e))
            raise e

    def draw_polygon(self):
        try:
            self.active_draw_mode = "POLYGON"
            self.canvas.old_coords = None
            return False
        except Exception as e:
            print("Exception on draw polygon: {} {}".format(type(e), e))
            raise e

    def import_file(self):
        try:
            filename = filedialog.askopenfilename(
                initialdir=BASE_DIR, title="Selecione o aquivo JSON.",
                filetypes=(("Arquivos JSON", "*.json"), ("todos os arquivos", "*.*"))
            )
            import_json(filename=filename, window=self)
            return False
        except Exception as e:
            print("Exception on import_file: {} {}".format(type(e), e))
            raise e

    def export_file(self):
        try:
            export_json(window=self)
        except Exception as e:
            print("Exception on export_file: {} {}".format(type(e), e))
            raise e
