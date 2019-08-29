
import cmath
class Circle:

    def __init__(self, window, x, y, radius):
        self.window = window
        self.x = x
        self.radius = radius
        self.y = y

    def build_circle(self):
        angle = 1
        for angle in range(0, 360):
            x1 = self.x + self.radius * cmath.cos(angle)
            y1 = self.y + self.radius * cmath.sin(angle)
            draw = self.window.canvas.create_rectangle((x1, y1) * 2, fill="#000000", outline="#000000")
            angle = angle + 1










