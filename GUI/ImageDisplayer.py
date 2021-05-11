from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

class ImageDisplayer:
	"""displayer of a segment of an image"""
	def __init__(self, root, width, height, row=1, column=2):
		self.width = width
		self.height = height
		self.label = Label(root);
		self.label.grid(row=row, column=column)

	def set_image(self, img):
		self.current_image = img

	def change_segment(self, to_select):
		"""change the segment of current_image wich is going to be show"""
		self.current_segment = self.current_image.crop(to_select)
		self.current_segment = ImageTk.PhotoImage(self.current_segment)
		self.show()

	def show(self):
		self.label.configure(image=self.current_segment)
