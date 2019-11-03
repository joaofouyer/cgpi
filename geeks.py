import os
from tkinter import *
from tkinter.ttk import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='GeeksforGeeks', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file=r"{}/static/icon/circle-regular.png".format(BASE_DIR)).subsample(5)

# here, image option is used to
# set image on button
Button(root, text='Click Me !', image=photo).pack(side=TOP)

mainloop()