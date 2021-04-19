__author__ = "Hernandez Hernandez Bernado and Salazar Alanis Victor Yoguel"
# __copyright__ = ""
__credits__ = ["Hernandez Hernandez Bernado", "Salazar Alanis Victor Yoguel"]
# __license__ = "GPL"
# __version__ = "0.0.1"
__date__ = "2021-03-15"
__status__ = "Production"


# Built-in packages
import os

# Third party packages
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from pydicom import dcmread

#const
width_right_image = 1200
height_right_image = 700

def pixel_array_to_gray(pixel_array):
  """Return a uint8 pixel array representation of 
  the original pixel array with values from 0 to 255
  """
  pixel_array = pixel_array.astype("uint32")
  pixel_array -= np.amin(pixel_array)
  max_val = np.amax(pixel_array)
  pixel_array *= 255
  pixel_array //= max_val
  return Image.fromarray(pixel_array.astype("uint8"))
  
def dcm_to_PIL_image_gray(fpath):
  """Read a DICOM file and return it as a gray scale PIL image"""
  ds = dcmread(fpath)
  return pixel_array_to_gray(ds.pixel_array)  # Aun se ve borroso

def open_mini_image(img):
  """open and resize img of the left"""
  # Resize image
  if img.size[0] > 500: #adjust height
    fixed_height = float(500)
    height_percent = (fixed_height / float(img.size[1]))
    width_size = int((float(img.size[0]) * float(height_percent)))
    img = img.resize((int(width_size), int(fixed_height)))
  if img.size[1] > 300: #adjust width
    fixed_width = float(300)
    width_percent = (fixed_width / float(img.size[0]))
    height_size = int((float(img.size[1]) * float(width_percent)))
    img = img.resize((int(fixed_width), int(height_size)))
  # Show image
  global leftImg
  leftImg = ImageTk.PhotoImage(img)
  leftSide.create_image(0, 0, anchor=NW, image=leftImg)

def change_zoom_image(originalImg, to_select):
  """open and cut img of the right"""
  img = originalImg.crop(to_select)
  # Show image
  img = ImageTk.PhotoImage(img)
  zoomImg.configure(image = img)
  zoomImg.image = img

def click_on_open():
  """Select a DICOM file and show it on screen using the PIL packege"""
  global root
  global originalImg
  # Open image
  root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
  open_image(root.filename)

def show(x, y):
  open_mini_image(originalImg)
  xsize = float(width_right_image*leftImg.width())/float(originalImg.size[0])
  ysize = float(height_right_image*leftImg.height())/float(originalImg.size[1])
  x = max(x, xsize/2)
  y = max(y, ysize/2)
  x = min(x, leftImg.width()-xsize/2)
  y = min(y, leftImg.height()-ysize/2)
  coord = [
      max([0, int(float(originalImg.size[0]*x)/float(leftImg.width())) - width_right_image/2]),
      max([0, int(float(originalImg.size[1]*y)/float(leftImg.height())) - height_right_image/2]), 
      min([originalImg.size[0], int(float(originalImg.size[0]*x)/float(leftImg.width())) + width_right_image/2]), 
      min([originalImg.size[1], int(float(originalImg.size[1]*y)/float(leftImg.height())) + height_right_image/2])
  ]
  change_zoom_image(originalImg, coord)
  leftSide.create_rectangle(x-xsize/2, y-ysize/2, x+xsize/2, y+ysize/2, outline="#05f")

def open_image(fpath):
  """open an image"""
  global originalImg
  originalImg = dcm_to_PIL_image_gray(fpath)
  show(float(34), float(28))

def fullScreen():
  """screen in full size"""
  #getting screen width and height of display
  width= root.winfo_screenwidth() 
  height= root.winfo_screenheight()
  #setting tkinter window size
  root.geometry("%dx%d" % (width, height))
  root.title("Geeeks For Geeks")

def callback(event):
    global originalImg
    show(event.x, event.y)

  
if __name__ == "__main__":
  # Init window
  root = Tk()
  root.title("visualización de mamografias")
  fullScreen()
  # Add Buttons
  openButton = Button(root, text = "Abrir", command=click_on_open)
  openButton.grid(row = 0, column = 0)
  # Init img
  originalImg = Image.open("emptyIMG.jpg")
  leftSide = Canvas(root, width = 305, height = 505)
  leftSide.grid(row = 1, column = 0)
  leftImg = ImageTk.PhotoImage(originalImg)
  leftSide.create_image(0, 0, anchor=NW, image=leftImg)
  leftSide.bind("<Button-1>", callback)
  zoomImg = Label(root, image = leftImg)
  zoomImg.grid(row = 1, column = 2)
  open_image('example.dcm')

  # Start window
  root.mainloop();

