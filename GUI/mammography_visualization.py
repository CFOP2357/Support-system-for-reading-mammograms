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

def openMiniImg(fpath):
  """abre la imagen miniatura en la izquierda"""
  img = dcm_to_PIL_image_gray(fpath)
  # Resize image
  if img.size[0] > 500: #adjust height
    fixed_height = float(500)
    height_percent = (fixed_height / float(img.size[1]))
    width_size = int((float(img.size[0]) * float(height_percent)))
    img = img.resize((int(width_size), int(fixed_height)))
  if img.size[1] > 300: #adjusr width
    fixed_width = float(300)
    width_percent = (fixed_width / float(img.size[0]))
    height_size = int((float(img.size[1]) * float(width_percent)))
    img = img.resize((int(fixed_width), int(height_size)))
  # Show image
  img = ImageTk.PhotoImage(img)
  currentImage.configure(image = img)
  currentImage.image = img



def click_on_open():
  """Select a DICOM file and show it on screen using the PIL packege"""
  # Open image
  root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
  openMiniImg(root.filename)

  

def fullScreen():
  """screen in full size"""
  #getting screen width and height of display
  width= root.winfo_screenwidth() 
  height= root.winfo_screenheight()
  #setting tkinter window size
  root.geometry("%dx%d" % (width, height))
  root.title("Geeeks For Geeks")
  
  
if __name__ == "__main__":
  # Init window
  root = Tk()
  root.title("visualización de mamografias")
  fullScreen()

  # Add Buttonsñññ
  openButton = Button(root, text = "Abrir", command=click_on_open)
  openButton.grid(row = 0, column = 0)

  # Init img
  img = ImageTk.PhotoImage(Image.open("emptyIMG.jpg"))
  currentImage = Label(root, image = img)
  currentImage.grid(row = 1, column = 0)
  openMiniImg('example.dcm')

  # Start window
  root.mainloop();

