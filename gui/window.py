# coding: utf-8
from structures.action import Action
from primitives.point_graph import PointGraph
from primitives.circle_graph import CircleGraph
from primitives.line_graph import LineGraph
from primitives.rectangle_graph import RectangleGraph
from gui.viewport import Viewport
import sys

# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED
else:
    from tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED

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
        self.canvas = Canvas(self.root, width=self.width, height=self.height, bg=self.background)
        self.actions = actions

        sidebar = Frame(width=150, height=self.height, bg="#282A36", borderwidth=2)
        sidebar.pack(side=LEFT)

        self.point_btn = Button(self.root, BTN_CONFIG, text="Ponto", command=self.draw_point)
        self.line_btn = Button(self.root, BTN_CONFIG, text="Reta", command=self.draw_line)
        self.circle_btn = Button(self.root, BTN_CONFIG, text="Círculo", command=self.draw_circle)
        self.rectangle_btn = Button(self.root, BTN_CONFIG, text="Retângulo", command=self.draw_rectangle)
        self.undo_btn = Button(self.root, BTN_CONFIG, text="Desfazer", state=DISABLED, command=self.undo)
        self.redo_btn = Button(self.root, BTN_CONFIG, text="Refazer", state=DISABLED, command=self.redo)

        self.point_btn.place(height=25, width=130, x=10, y=10)
        self.line_btn.place(height=25, width=130, x=10, y=45)
        self.circle_btn.place(height=25, width=130, x=10, y=80)
        self.rectangle_btn.place(height=25, width=130, x=10, y=115)
        self.undo_btn.place(height=25, width=130, x=10, y=150)
        self.redo_btn.place(height=25, width=130, x=10, y=185)

        self.canvas = Canvas(self.root, width=self.width-150, height=self.height, bg=self.background)
        self.viewport = Viewport(root=self.root, width=130, height=130, background=self.background)
        self.viewport.canvas.place(x=10, y=self.height-140)


        self.active_draw_mode = None
        self.canvas.old_coords = None

    def open(self):
        try:
            self.refresh()
            return self.canvas.pack(side=RIGHT)
        except Exception as e:
            print("Exception in Window.open: ", e)

    def mainloop(self):
        try:
            self.open()
            self.canvas.bind('<ButtonPress-1>', self.click_event)
            mainloop()
            return False
        except Exception as e:
            print('mainloop: ', e)

    def update_undo_btn_state(self):
        try:
            if len(self.actions.actions_stack):
                self.undo_btn.config(state="normal")
            else:
                self.undo_btn.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update_undo_btn_state: ", e)
            return True

    def update_redo_btn_state(self):
        try:
            if len(self.actions.undo_stack):
                self.redo_btn.config(state="normal")
            else:
                self.redo_btn.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update_redo_btn_state: ", e)
            return True

    def refresh(self):
        try:
            self.update_redo_btn_state()
            self.update_undo_btn_state()
        except Exception as e:
            print("Exception on refresh: ", e)
            return True

    def undo(self):
        try:
            return self.actions.undo(window=self)
        except Exception as e:
            print("Exception on window.undo: ", e)
            return True

    def redo(self):
        try:
            return self.actions.redo(window=self)
        except Exception as e:
            print("Exception on window.redo: ", e)
            return True

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

                else:
                    self.canvas.old_coords = point
            return False
        except Exception as e:
            print("Exception on click_event:", e)
            return True

    def draw_point(self):
        try:
            self.active_draw_mode = "POINT"
            return False
        except Exception as e:
            print("Exception on draw_point:", e)
            return True

    def draw_line(self):
        try:
            self.active_draw_mode = "LINE"
            return False
        except Exception as e:
            print("Exception on draw_line:", e)
            return True

    def draw_circle(self):
        try:
            self.active_draw_mode = "CIRCLE"
            return False
        except Exception as e:
            print("Exception on draw_circle:", e)
            return True

    def draw_rectangle(self):
        try:
            self.active_draw_mode = "RECTANGLE"
            return False
        except Exception as e:
            print("Exception on draw_rectangle:", e)
            return True
