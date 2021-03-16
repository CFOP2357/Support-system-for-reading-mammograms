
__author__ = "Hernandez Hernandez Bernado and Salazar Alanís Víctor Yoguel"
# __copyright__ = ""
__credits__ = ["Hernandez Hernandez Bernado", "Salazar Alanís Víctor Yoguel"]
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
  pixel_array = pixel_array.astype("float")
  pixel_array -= np.amin(pixel_array)
  pixel_array /= np.amax(pixel_array)
  pixel_array *= 255
  return Image.fromarray(pixel_array.astype("uint8"))

  
def dcm_to_PIL_image_gray(fpath):
  """Read a DICOM file and return it as a gray scale PIL image"""
  
  ds = dcmread(fpath)

  return pixel_array_to_gray(ds.pixel_array)  # Aun se ve borroso


def click_on_open():
  """Select a DICOM file and show it on screen using the PIL packege"""
  # Open image
  root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
  img = dcm_to_PIL_image_gray(root.filename)

  # Resize image
  fixed_height = float(600)
  height_percent = (fixed_height / float(img.size[1]))
  width_size = int((float(img.size[0]) * float(height_percent)))
  img = img.resize((int(width_size), int(fixed_height)))
  
  # Show image
  img = ImageTk.PhotoImage(img)

  currentImage.configure(image = img)
  currentImage.image = img
  
  
if __name__ == "__main__":
  # Init window
  root = Tk()
  root.title("visualización de mamografias")

  # Add Buttons
  openButton = Button(root, text = "Abrir", command=click_on_open)
  openButton.grid(row = 0, column = 0);

  # Init img
  img = ImageTk.PhotoImage(Image.open("emptyIMG.jpg"))
  currentImage = Label(root, image = img)
  currentImage.grid(row = 1, column = 0)

  # Start window
  root.mainloop();
