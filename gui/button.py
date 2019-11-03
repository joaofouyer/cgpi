import sys

if sys.version_info[0] < 3:
    from Tkinter import Button, DISABLED, CENTER
else:
    from tkinter import Button, DISABLED, CENTER

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
            self.line = Button(root, BTN_CONFIG, image=icons.line, command=commands['draw_line'])
            self.circle = Button(root, BTN_CONFIG, image=icons.circle, anchor=CENTER, command=commands['draw_circle'])
            self.rectangle = Button(root, BTN_CONFIG, image=icons.square, command=commands['draw_rectangle'])
            self.polygon = Button(root, BTN_CONFIG, image=icons.polygon, command=commands['draw_polygon'])
            self.undo = Button(root, BTN_CONFIG, image=icons.undo, state=DISABLED, command=commands['undo'])
            self.redo = Button(root, BTN_CONFIG, image=icons.redo, state=DISABLED, command=commands['redo'])
            self.import_file = Button(root, BTN_CONFIG, image=icons.import_file, command=commands['import_file'])
            self.export = Button(root, BTN_CONFIG, image=icons.export, state=DISABLED, command=commands['export_file'])
            self.clipping = Button(root, BTN_CONFIG, image=icons.clipping, command=commands['set_clipping_area'])

            self.line.place(height=40, width=40, x=25, y=10)
            self.circle.place(height=40, width=40, x=90, y=10)
            self.rectangle.place(height=40, width=40, x=25, y=60)
            self.polygon.place(height=40, width=40, x=90, y=60)
            self.undo.place(height=40, width=40, x=25, y=110)
            self.redo.place(height=40, width=40, x=90, y=110)
            self.import_file.place(height=40, width=40, x=25, y=160)
            self.export.place(height=40, width=40, x=90, y=160)
            self.clipping.place(height=40, width=40, x=25, y=210)
        except Exception as e:
            print("Exception on button constructor: {} {}".format(type(e), e))
            raise e
