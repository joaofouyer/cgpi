histogram = img.image.histogram()
l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]

plt.figure(0)
if len(l1):
    for i in range(0, 256):
        plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)
if len(l2):
    for i in range(0, 256):
        plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)
if len(l3):
    for i in range(0, 256):
        plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)

canvas = FigureCanvasTkAgg(plt.figure(), master=self.sidebar)
canvas.draw()
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, self.sidebar)
toolbar.update()
canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=1)