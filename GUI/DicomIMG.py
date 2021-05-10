from pydicom import dcmread
import cv2 as cv
import numpy as np
from PIL import ImageTk, Image

def unsharp_mask(image, kernel_size=(5, 5), sigma=10000.0, amount=100.0, threshold=10000.0):
    """Return a sharpened version of the image, using an unsharp mask."""
    blurred = cv.GaussianBlur(image, kernel_size, sigma)
    sharpened = float(amount + 1) * image - float(amount) * blurred
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))
    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)
    sharpened = sharpened.round().astype(np.uint8)
    return sharpened

def pixel_array_to_gray(pixel_array):
    """Return a uint8 pixel array representation of
    the original pixel array with values from 0 to 255
    """
    pixel_array = pixel_array.astype("float32")
    pixel_array -= np.amin(pixel_array)
    max_val = np.amax(pixel_array)
    pixel_array *= 255
    pixel_array /= max_val
    return pixel_array

def dcm_to_PIL_image_gray(fpath):
    """Read a DICOM file and return it as a gray scale PIL image"""
    ds = dcmread(fpath)
    img = unsharp_mask(pixel_array_to_gray(np.float32(ds.pixel_array)))
    return Image.fromarray(img)  # Aun se ve borroso
