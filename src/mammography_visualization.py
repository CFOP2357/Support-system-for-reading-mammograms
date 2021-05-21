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
import tkinter
from tkinter import *
from tkinter import filedialog

import DicomIMG
from SelectionImage import *
from ImageDisplayer import *

is_filtered = False

def update_image_filter():
    if is_filtered:
        global filtered_image
        selection_image.set_image(filtered_image)
        image_displayer.image = filtered_image
    else:
        global original_image
        selection_image.set_image(original_image)
        image_displayer.image = original_image
    selection_image.set_segment_position()

def click_on_filter():
    global filter_button_text
    global is_filtered
    if is_filtered:
        is_filtered = False
        filter_button_text.set("Filtrar")
    else:
        is_filtered = True
        filter_button_text.set("Mostrar Original");
    update_image_filter()

def open_image(file_path):
    """open an image"""
    global selection_image
    global image_displayer
    global original_image
    global filtered_image
    [original_image, filtered_image] = DicomIMG.dcm_to_pil_image_gray(file_path)
    global is_filtered
    is_filtered = False
    filter_button_text.set("Filtrar")
    update_image_filter()


def click_on_open():
    """Select a DICOM file and show it on screen using the PIL packege"""
    global root
    root.filename = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=(("DICOM", "*.dcm"), ("", "")))
    open_image(root.filename)


def fullscreen():
    """screen in full size"""
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.geometry("%dx%d" % (width, height))


if __name__ == "__main__":
    root = tkinter.Tk()
    root.title("Visualización de mamografias")
    fullscreen()
    open_button = Button(root, text="Abrir", command=click_on_open)
    open_button.grid(row=0, column=0)
    filter_button_text = tkinter.StringVar();
    filter_button = Button(root, textvariable=filter_button_text, command=click_on_filter)
    filter_button.grid(row=0, column=2)
    filter_button_text.set("Filtrar")
    image_displayer = ImageDisplayer(root, width=1200, height=750)
    selection_image = SelectionImage(root, width=305, height=505, displayer=image_displayer)
    #oppening only once at the begining put the rectangle on a "random position" i dont know why, is a bugg
    open_image('example.dcm')
    open_image('example.dcm')
    root.mainloop()
