class Animation:
    def __init__(self, window):
        self.frame = []
        self.window = window

    def animate(self, speed=10):
        try:
            if (len(self.frame)):
                f = self.frame.pop(0)
                f.window = self.window
                f.draw()
                self.window.canvas.after(speed, self.animate)
        except Exception as e:
            print(e)

    def append_frame(self, frame):
        self.frame.append(frame)