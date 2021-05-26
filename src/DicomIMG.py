from pydicom import dcmread
import cv2 as cv
import numpy as np
from PIL import Image


def unsharp_mask(image, kernel_size: tuple = (5, 5), sigma: float = 10000.0, amount: float = 100.0,
                 threshold: float = 10000.0) -> np.array:
    """Return a sharpened version of the image, using an unsharp mask."""
    # Blur image
    blurred = cv.GaussianBlur(image, kernel_size, sigma)

    # Sharp using the difference between the images (unsharp_mask)
    sharpened = float(amount + 1) * image - float(amount) * blurred

    # Make sure that all pixel values are in the interval [0, 255]
    sharpened = np.maximum(sharpened, np.zeros(sharpened.shape))
    sharpened = np.minimum(sharpened, 255 * np.ones(sharpened.shape))

    if threshold > 0:
        low_contrast_mask = np.absolute(image - blurred) < threshold
        np.copyto(sharpened, image, where=low_contrast_mask)  # Do not change pixels where low_contrast_mask is true

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
    return pixel_array.astype("uint8")


def apply_clahe(img):
    """Apply CLAHE filter using GPU"""

    clahe = cv.createCLAHE()  # crete clahe parameters

    img_umat = cv.UMat(img)  # send img to gpu

    img_umat = clahe.apply(img_umat)

    # Normalize image to the interval [0, 255]
    img_umat = cv.normalize(img_umat, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)

    return img_umat.get()  # recover img from gpu


def dcm_to_pil_image_gray(file_path):
    """Read a DICOM file and return it as a gray scale PIL image"""
    ds = dcmread(file_path)
    # Get the image after apply clahe
    img_filtered = Image.fromarray(apply_clahe(ds.pixel_array).astype("uint8"))
    # Normalize original image to the interval [0, 255]
    img = cv.normalize(ds.pixel_array, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_8U)
    img = Image.fromarray(img.astype("uint8"))
    return [img, img_filtered]
