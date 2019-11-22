import sys

if sys.version_info[0] < 3:
    from Tkinter import Button, DISABLED, CENTER, colorchooser
else:
    from tkinter import Button, DISABLED, CENTER, colorchooser

BTN_CONFIG = {
    "border": "0",
    "activebackground": "#BED8D4",
    "background": "#E5E8E8",
    "bd": "0",
    "borderwidth": 0,
    "foreground": "#5B5B63",
    "activeforeground": "#5B5B63",
    "font": "Bold",
}


class SidebarButton:
    def __init__(self, root, icons, commands):
        try:
            self.line = Button(root, BTN_CONFIG, image=icons.line, command=self.draw_line)
            self.circle = Button(root, BTN_CONFIG, image=icons.circle, anchor=CENTER, command=self.draw_circle)
            self.rectangle = Button(root, BTN_CONFIG, image=icons.square, command=self.draw_rectangle)
            self.polygon = Button(root, BTN_CONFIG, image=icons.polygon, command=self.draw_polygon)
            self.undo = Button(root, BTN_CONFIG, image=icons.undo, state=DISABLED, command=commands['undo'])
            self.redo = Button(root, BTN_CONFIG, image=icons.redo, state=DISABLED, command=commands['redo'])
            self.import_file = Button(root, BTN_CONFIG, image=icons.import_file, command=commands['import_file'])
            self.export = Button(root, BTN_CONFIG, image=icons.export, state=DISABLED, command=commands['export_file'])
            self.clipping = Button(root, BTN_CONFIG, image=icons.clipping, command=self.set_clipping_area)
            self.color = Button(root, BTN_CONFIG, image=icons.color, command=self.set_color)
            self.erase = Button(root, BTN_CONFIG, image=icons.erase)

            self.line.place(height=40, width=40, x=25, y=10)
            self.circle.place(height=40, width=40, x=90, y=10)
            self.rectangle.place(height=40, width=40, x=25, y=60)
            self.polygon.place(height=40, width=40, x=90, y=60)
            self.undo.place(height=40, width=40, x=25, y=110)
            self.redo.place(height=40, width=40, x=90, y=110)
            self.import_file.place(height=40, width=40, x=25, y=160)
            self.export.place(height=40, width=40, x=90, y=160)
            self.clipping.place(height=40, width=40, x=25, y=210)
            self.erase.place(height=40, width=40, x=90, y=210)
            self.color.place(height=40, width=40, x=25, y=260)

            self.active = None
            self.active_color = "#000000"

        except Exception as e:
            print("Exception on button constructor: {} {}".format(type(e), e))
            raise e

    def update_undo_btn_state(self, actions_stack):
        try:
            if len(actions_stack):
                self.undo.config(state="normal")
                self.export.config(state="normal")
            else:
                self.undo.config(state="disabled")
                self.export.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update undo btn state: {} {}".format(type(e), e))
            raise e

    def update_redo_btn_state(self, undo_stack):
        try:
            self.redo.config(state="normal") if len(undo_stack) else self.redo.config(state="disabled")
            return False
        except Exception as e:
            print("Exception on update redo btn state: {} {}".format(type(e), e))
            raise e

    def draw_point(self):
        try:
            self.active = "POINT"
            return False
        except Exception as e:
            print("Exception on draw point: {} {}".format(type(e), e))
            raise e

    def draw_line(self):
        try:
            self.active = "LINE"
            return False
        except Exception as e:
            print("Exception on draw line: {} {}".format(type(e), e))
            raise e

    def draw_circle(self):
        try:
            self.active = "CIRCLE"
            return False
        except Exception as e:
            print("Exception on draw circle: {} {}".format(type(e), e))
            raise e

    def draw_rectangle(self):
        try:
            self.active = "RECTANGLE"
            return False
        except Exception as e:
            print("Exception on draw rectangle: {} {}".format(type(e), e))
            raise e

    def draw_polygon(self):
        try:
            self.active = "POLYGON"
            return False
        except Exception as e:
            print("Exception on draw polygon: {} {}".format(type(e), e))
            raise e

    def set_clipping_area(self):
        try:
            self.active = "CLIPPING"
            return False
        except Exception as e:
            print("Exception on set_clipping_area: {} {}".format(type(e), e))
            raise e

    def set_color(self):
        try:
            self.active_color = colorchooser.askcolor()[1]
            print(self.active_color)
        except Exception as e:
            print("Exception on set_color: {} {}".format(type(e), e))
            raise e
