from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("imagen");

myImg = ImageTk.PhotoImage(Image.open("../data/test.jpeg"))
imageLabel = Label(image=myImg)
imageLabel.pack()

root.mainloop()