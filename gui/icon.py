import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if sys.version_info[0] < 3:
    from Tkinter import PhotoImage
else:
    from tkinter import PhotoImage


class Icon:
    def __init__(self):
        try:
            self.circle = PhotoImage(file=r"{}/static/icon/circle.png".format(BASE_DIR)).subsample(2)
            self.clipping = PhotoImage(file=r"{}/static/icon/clipping.png".format(BASE_DIR)).subsample(2)
            self.color = PhotoImage(file=r"{}/static/icon/color.png".format(BASE_DIR)).subsample(2)
            self.export = PhotoImage(file=r"{}/static/icon/export.png".format(BASE_DIR)).subsample(2)
            self.import_file = PhotoImage(file=r"{}/static/icon/import.png".format(BASE_DIR)).subsample(2)
            self.line = PhotoImage(file=r"{}/static/icon/line.png".format(BASE_DIR)).subsample(2)
            self.polygon = PhotoImage(file=r"{}/static/icon/polygon.png".format(BASE_DIR)).subsample(2)
            self.redo = PhotoImage(file=r"{}/static/icon/redo.png".format(BASE_DIR)).subsample(2)
            self.square = PhotoImage(file=r"{}/static/icon/square.png".format(BASE_DIR)).subsample(2)
            self.undo = PhotoImage(file=r"{}/static/icon/undo.png".format(BASE_DIR)).subsample(2)
        except Exception as e:
            print("Exception on icon constructor: {} {}".format(type(e), e))
            raise e
