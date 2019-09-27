# coding: utf-8
from structures.action import Action
from primitives.point_graph import PointGraph
from primitives.circle_graph import CircleGraph
from primitives.line_graph import LineGraph
from primitives.rectangle_graph import RectangleGraph
from gui.viewport import Viewport
from gui.sidebar import Sidebar
import sys

# Importante para garantir que funcione em python2 e em python3.

if sys.version_info[0] < 3:
    from Tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED
else:
    from tkinter import Tk, Canvas, mainloop, Button, Frame, LEFT, RIGHT, SUNKEN, DISABLED


class Window:
    def __init__(self, title="PUC-SP", width=500, height=500, background="#ffffff", actions=Action()):
        self.title = title
        self.width = width
        self.height = height
        self.background = background
        self.root = Tk()
        self.root.title(self.title)
        self.actions = actions
        self.sidebar = Sidebar(window=self, width=(self.width*0.17), height=self.height)
        self.canvas_width = self.width - (self.width*0.17)
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.height, bg=self.background)
        self.viewport = Viewport(root=self.root, width=self.canvas_width * 0.15, height=(self.height*0.15), background=self.background)
        self.viewport.canvas.place(x=10, y=(self.height - self.height*0.17))
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

    def refresh(self):
        try:
            self.sidebar.update_redo_btn_state()
            self.sidebar.update_undo_btn_state()
        except Exception as e:
            print("Exception on refresh: ", e)
            return True

    def click_event(self, event):
        try:
            point = PointGraph(x=event.x, y=event.y, window=self)
            if self.sidebar.active_draw_mode == "POINT":
                point.draw(append_action=True)
                self.canvas.old_coords = None
            else:
                if self.canvas.old_coords:
                    p1 = self.canvas.old_coords
                    p2 = point
                    if self.sidebar.active_draw_mode == "LINE":
                        line = LineGraph(p1=p1, p2=p2)
                        line.draw(window=self, animation=False)
                        self.canvas.old_coords = None
                    elif self.sidebar.active_draw_mode == "CIRCLE":
                        line = LineGraph(p1=p1, p2=p2)
                        circle = CircleGraph(center=p1, radius=line.length)
                        circle.draw(window=self)
                        self.canvas.old_coords = None
                    elif self.sidebar.active_draw_mode == "RECTANGLE":
                        rectangle = RectangleGraph(p1=p1, p2=p2)
                        rectangle.draw(window=self)
                        self.canvas.old_coords = None

                else:
                    self.canvas.old_coords = point
            return False
        except Exception as e:
            print("Exception on click_event:", e)
            return True
