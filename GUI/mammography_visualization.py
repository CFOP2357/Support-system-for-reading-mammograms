
__author__ = "Hernandez Hernandez Bernado and Salazar Alanís Víctor Yoguel"
# __copyright__ = ""
__credits__ = ["Hernandez Hernandez Bernado", "Salazar Alanís Víctor Yoguel"]
# __license__ = "GPL"
# __version__ = "0.0.1"
__date__ = "2021-03-15"
__status__ = "Production"


import os

import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
from pydicom import dcmread

def pixel_array_to_PIL_img_gray(pixel_array):
  pixel_array = pixel_array.astype("float")
  pixel_array -= np.amin(pixel_array)
  pixel_array /= np.amax(pixel_array)
  pixel_array *= 255
  return Image.fromarray(pixel_array.astype("uint8"))
  
def dcm_to_PIL_image_gray(fpath):
  ds = dcmread(fpath)

  return pixel_array_to_PIL_img_gray(ds.pixel_array)  # Aun se ve borroso

def clickOnOpen():
  root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
  img = ImageTk.PhotoImage(dcm_to_PIL_image_gray(root.filename))
  currentImage.configure(image = img)
  currentImage.image = img
  #my_image = 

root = Tk()
root.title("visualización de mamografias")

openButton = Button(root, text = "Abrir", command=clickOnOpen)
openButton.grid(row = 0, column = 0);

img = ImageTk.PhotoImage(Image.open("emptyIMG.jpg"))
currentImage = Label(root, image = img)
currentImage.grid(row = 1, column = 0)

root.mainloop();
