import tkinter
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import typing


class ImageDisplayer:
	"""Display a segment of an image"""
	def __init__(self, root: tkinter.Tk, width: int, height: int, row: int = 1, column: int = 2):
		self.width = width
		self.height = height
		self.label = Label(root)
		self.label.grid(row=row, column=column)
		self.current_image = None
		self.current_segment = None

	@property
	def image(self):
		return self.current_image

	@image.setter
	def image(self, img):
		"""Update image"""
		self.current_image = img

	def change_segment(self, to_select):
		"""change the segment of image wich is going to be show"""
		self.current_segment = self.image.crop(to_select)
		self.current_segment = ImageTk.PhotoImage(self.current_segment)
		self.show()

	def show(self):
		"""show the segment image"""
		self.label.configure(image=self.current_segment)
