from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

import DicomIMG

# Const
width_right_image = 1200
height_right_image = 750

def open_mini_image(img):
    """open and resize img of the left"""
    # Resize image
    if img.size[0] > 500:  # adjust height
        fixed_height = float(500)
        height_percent = (fixed_height / float(img.size[1]))
        width_size = int((float(img.size[0]) * float(height_percent)))
        img = img.resize((int(width_size), int(fixed_height)))
    if img.size[1] > 300:  # adjust width
        fixed_width = float(300)
        width_percent = (fixed_width / float(img.size[0]))
        height_size = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((int(fixed_width), int(height_size)))
    # Show image
    global leftImg
    global leftSide
    leftImg = ImageTk.PhotoImage(img)
    leftSide.create_image(0, 0, anchor=NW, image=leftImg)


def change_zoom_image(originalImg, to_select):
    """open and cut img of the right"""
    img = originalImg.crop(to_select)
    # Show image
    img = ImageTk.PhotoImage(img)
    zoomImg.configure(image=img)
    zoomImg.image = img


def show(x, y):
    global leftSide
    leftSide.delete("rectangle")
    xsize = float(width_right_image * leftImg.width()) / float(originalImg.size[0])
    ysize = float(height_right_image * leftImg.height()) / float(originalImg.size[1])
    x = max(x, xsize / 2)
    y = max(y, ysize / 2)
    x = min(x, leftImg.width() - xsize / 2)
    y = min(y, leftImg.height() - ysize / 2)
    coord = [
        max([0, int(float(originalImg.size[0] * x) / float(leftImg.width())) - width_right_image / 2]),
        max([0, int(float(originalImg.size[1] * y) / float(leftImg.height())) - height_right_image / 2]),
        min([originalImg.size[0],
             int(float(originalImg.size[0] * x) / float(leftImg.width())) + width_right_image / 2]),
        min([originalImg.size[1],
             int(float(originalImg.size[1] * y) / float(leftImg.height())) + height_right_image / 2])
    ]
    change_zoom_image(originalImg, coord)
    leftSide.create_rectangle(x - xsize / 2, y - ysize / 2, x + xsize / 2, y + ysize / 2, outline="#05f",
                              tag="rectangle")


def open_image(fpath):
    """open an image"""
    global originalImg
    originalImg = DicomIMG.dcm_to_PIL_image_gray(fpath)
    open_mini_image(originalImg)
    show(float(34), float(28))