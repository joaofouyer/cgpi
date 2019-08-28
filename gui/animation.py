# coding: utf-8


class Animation:
    def __init__(self, window, speed=10):
        self.frame = []
        self.window = window
        self.speed = speed

    def animate(self):
        try:
            if len(self.frame):
                f = self.frame.pop(0)
                f.window = self.window
                f.draw()
                self.window.canvas.after(self.speed, self.animate)
        except Exception as e:
            print(e)

    def append_frame(self, frame):
        self.frame.append(frame)
