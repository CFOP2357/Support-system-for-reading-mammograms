
__author__ = "Hernandez Hernandez Bernado and Salazar Alanís Víctor Yoguel"
# __copyright__ = ""
__credits__ = ["Hernandez Hernandez Bernado", "Salazar Alanís Víctor Yoguel"]
# __license__ = "GPL"
# __version__ = "0.0.1"
__date__ = "2021-03-15"
__status__ = "Production"


import os

import numpy as np
from PIL import Image
from pydicom import dcmread

def pixel_array_to_PIL_img_gray(pixel_array):
  pixel_array = pixel_array.astype("float")
  pixel_array -= np.amin(pixel_array)
  pixel_array /= np.amax(pixel_array)
  pixel_array *= 255
  return Image.fromarray(pixel_array.astype("uint8"))
  
def dcm_to_jpg(fpath):
  ds = dcmread(fpath)

  im_out = pixel_array_to_PIL_img_gray(ds.pixel_array)  # Aun se ve borroso
  
  # Get filename with .jpg extension instead of .dcm
  jpg_fpath = os.path.splitext(fpath)[0] + ".jpg" 

  im_out.save(jpg_fpath)  # Guargar imagen en formato jpg

  return jpg_fpath