from tkinter import *
from PIL import ImageTk
from type_definitions import *
from ImageDisplayer import ImageDisplayer


class SelectionImage:
    """SelectionImage selects a rectangular segment from an image"""
    width_right_image = 1200
    height_right_image = 750
    width = 1
    height = 1

    def __init__(self, root: tkinter.Tk, width: int, height: int, displayer: ImageDisplayer, row: int = 1,
                 column: int = 0) -> None:
        self.root = root
        self.selection_side = Canvas(root, width=305, height=505)
        self.selection_side.grid(row=row, column=column)  # Set selection position
        self.selection_side.bind("<Button-1>", self.click)  # Activate interaction
        self.width = width
        self.height = height
        self.original_image = None
        self.current_image = None
        [self.x, self.y] = [width / 2, height / 2]
        # Displayer variables
        self.displayer = displayer
        self.width_right_image = displayer.width
        self.height_right_image = displayer.height

    def click(self, event) -> None:
        """click on one area of the selection image"""
        self.update_rectangle(event.x, event.y)  # Rectangle defining the area of visualization
        self.set_segment_position(event.x, event.y)  # Display zoom of the area inside of the rectangle

    def set_segment_position(self, x: int = -1, y: int = -1) -> None:
        """get te segment with center on {x, y}(if possible) and update display"""
        if [x, y] == [-1, -1]:
            [x, y] = [self.x, self.y]

        # Set center of the segment to the nearest valid coordinate to (x,y)
        [self.x, self.y] = [x, y]
        x = max(x, self.width / 2)
        y = max(y, self.height / 2)
        x = min(x, self.current_image.width() - self.width / 2)
        y = min(y, self.current_image.height() - self.height / 2)

        # Get coordinates defining the area to display
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
        self.displayer.segment = coord
        self.update_rectangle(x, y)

    def update_rectangle(self, x: int, y: int) -> None:
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

    @staticmethod
    def adjust_image_size(img: PilImage) -> PilImage:
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

    def set_image(self, image: PilImage) -> None:
        """set an image"""
        self.selection_side.delete("img")
        self.original_image = image
        self.current_image = self.adjust_image_size(self.original_image)
        self.current_image = ImageTk.PhotoImage(self.current_image)
        self.selection_side.create_image(0, 0, anchor=NW, image=self.current_image, tag="img")
