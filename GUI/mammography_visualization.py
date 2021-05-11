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
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

import DicomIMG
from SelectionImage import *
from ImageDisplayer import *

def open_image(fpath):
    """open an image"""
    global selection_image
    global image_displayer
    img = DicomIMG.dcm_to_PIL_image_gray(fpath)
    selection_image.set_image(img)
    image_displayer.set_image(img)
    selection_image.set_segment_position(0, 0)

def click_on_open():
    """Select a DICOM file and show it on screen using the PIL packege"""
    global root
    root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
    open_image(root.filename)

def fullscreen():
    """screen in full size"""
    width= root.winfo_screenwidth() 
    height= root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))

if __name__ == "__main__":
    root = Tk()
    root.title("visualización de mamografias")
    fullscreen()
    open_button = Button(root, text="Abrir", command=click_on_open)
    open_button.grid(row=0, column=0)
    image_displayer = ImageDisplayer(root, width=1200, height=750)
    selection_image = SelectionImage(root, width = 305, height = 505, displayer = image_displayer)
    open_image('example.dcm')

    # Start window
    root.mainloop()
