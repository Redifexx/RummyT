from tkinter import *

root = Tk()
#a = Label(root, text = "Hello World")
#.pack()

root.title("RummyT developed by Redifexx and K-Puig")
root.geometry('1280x720')
lbl = Label(root, text = "Welcome to RummyT!")
lbl.grid()

def clicked():
    lbl.configure(text = "TeeHee")

btn = Button(root, text = "Am I a Button?", fg = "blue", command = clicked)
btn.grid(column = 1, row = 0)




root.mainloop()