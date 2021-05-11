from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

class SelectionImage:
	"""SelectionImage selects a rectangular segment from an image"""
	current_image = Image.open("emptyIMG.jpg")
	width_right_image = 1200
	height_right_image = 750
	width = 1
	height = 1

	def clik(event):
		update_rectangle(event.x, event.y)
	    #show(event.x, event.y)

	def __init__(self, root, width, height):
		self.root = root
		self.selection_side = Canvas(root, width=305, height=505)
		self.selection_side.grid(row=1, column=0)
		self.selection_side.bind("<Button-1>", self.clik)
		self.width = width
		self.height = height

	def update_rectangle(self, x, y):
		"""change rectangle´s position to {x, y} """
		self.selection_side.delete("rectangle")
		width = float(width_right_image * current_image.width()) 
		width = width/float(originalImg.size[0])
		height = float(height_right_image * current_image.height()) 
		height = height/float(originalImg.size[1])
		x = max(x, width / 2)
		y = max(y, height / 2)
		x = min(x, current_image.width() - width / 2)
		y = min(y, current_image.height() - height / 2)
		self.selection_side.create_rectangle(
    		x - width / 2, y - height / 2, 
    		x + width / 2, y + height / 2, 
    		outline="#05f", tag="rectangle")

	def adjust_image(self):
	    """open and resize img of the left"""
	    if current_image.size[0] > 500:  # adjust height
	        fixed_height = float(500)
	        height_percent = (fixed_height / float(current_image.size[1]))
	        width_size = int((float(current_image.size[0]) * float(height_percent)))
	        current_image = current_image.resize((int(width_size), int(fixed_height)))
	    if current_image.size[1] > 300:  # adjust width
	        fixed_width = float(300)
	        width_percent = (fixed_width / float(current_image.size[0]))
	        height_size = int((float(current_image.size[1]) * float(width_percent)))
	        current_image = current_image.resize((int(fixed_width), int(height_size)))

	def set_image(self, image):
		"""set an image"""
		self.selection_side.delete("img")
		current_image = image
		self.adjust_image()
		self.selection_side.create_image(0, 0, anchor=NW, image=ImageTk.PhotoImage(current_image), tag="img")

		