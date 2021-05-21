import tkinter
from tkinter import *
from PIL import ImageTk
from type_definitions import *


class ImageDisplayer:
	"""Display a segment of an image"""
	def __init__(self, root: tkinter.Tk, width: int, height: int, row: int = 1, column: int = 2) -> None:
		self.width = width
		self.height = height
		self.label = Label(root)
		self.label.grid(row=row, column=column)
		self.current_image = None
		self.current_segment = None

	@property
	def image(self) -> PilImage:
		return self.current_image

	@image.setter
	def image(self, img: PilImage) -> None:
		"""Update image"""
		self.current_image = img

	@property
	def segment(self) -> TkImage:
		return self.current_segment

	@segment.setter
	def segment(self, to_select: Coord) -> None:
		"""change the segment of image which is going to be show"""
		self.current_segment = self.image.crop(to_select)
		self.current_segment = ImageTk.PhotoImage(self.current_segment)
		self.show()

	def change_segment(self, to_select: Coord) -> None:
		"""change the segment of image which is going to be show"""
		self.current_segment = self.image.crop(to_select)
		self.current_segment = ImageTk.PhotoImage(self.current_segment)
		self.show()

	def show(self) -> None:
		"""show the segment image"""
		self.label.configure(image=self.current_segment)
