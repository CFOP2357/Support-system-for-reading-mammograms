from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


class SelectionImage:
    """SelectionImage selects a rectangular segment from an image"""
    width_right_image = 1200
    height_right_image = 750
    width = 1
    height = 1

    def __init__(self, root, width, height, displayer, row=1, column=0):
        self.root = root
        self.selection_side = Canvas(root, width=305, height=505)
        self.selection_side.grid(row=row, column=column)
        self.selection_side.bind("<Button-1>", self.clik)
        self.width = width
        self.height = height
        self.displayer = displayer
        self.width_right_image = displayer.width
        self.height_right_image = displayer.height

    def clik(self, event):
        """click on one area of the selection image"""
        self.update_rectangle(event.x, event.y)
        self.set_segment_position(event.x, event.y)

    def set_segment_position(self, x, y):
        """get te segment with center on {x, y}(if possible) and update display"""
        x = max(x, self.width / 2)
        y = max(y, self.height / 2)
        x = min(x, self.current_image.width() - self.width / 2)
        y = min(y, self.current_image.height() - self.height / 2)
        coord = [
            int(float(self.original_image.size[0] * x) / float(
                self.current_image.width())) - self.width_right_image / 2,
            int(float(self.original_image.size[1] * y) / float(
                self.current_image.height())) - self.height_right_image / 2,
            int(float(self.original_image.size[0] * x) / float(
                self.current_image.width())) + self.width_right_image / 2,
            int(float(self.original_image.size[1] * y) / float(
                self.current_image.height())) + self.height_right_image / 2
        ]
        self.displayer.change_segment(coord)
        self.update_rectangle(x, y)

    def update_rectangle(self, x, y):
        """change rectangle´s position to {x, y} """
        self.selection_side.delete("rectangle")
        self.width = float(self.width_right_image * self.current_image.width())
        self.width = self.width / float(self.original_image.size[0])
        self.height = float(self.height_right_image * self.current_image.height())
        self.height = self.height / float(self.original_image.size[1])
        self.selection_side.create_rectangle(
            x - self.width / 2, y - self.height / 2,
            x + self.width / 2, y + self.height / 2,
            outline="#05f", tag="rectangle")

    def adjust_image_size(self, img):
        """open and resize img of the left"""
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
        return img

    def set_image(self, image):
        """set an image"""
        self.selection_side.delete("img")
        self.original_image = image
        self.current_image = self.adjust_image_size(self.original_image)
        self.current_image = ImageTk.PhotoImage(self.current_image)
        self.selection_side.create_image(0, 0, anchor=NW, image=self.current_image, tag="img")
