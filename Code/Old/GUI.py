from tkinter import *

keys = ["A", "B"]

window = Tk()
window.title("Blah Blah")
label = Label(window, text="Pinky: " + keys[0])
label.config(font=("Consolas",20))
label.pack(side=LEFT)

label = Label(window, text="Ring: " + keys[1])
label.config(font=("Consolas",20))
label.pack(side=RIGHT)


window.mainloop()
