"""
   Runs a powershell script to convert original pdfs into tiff files. Tiff files are then converted
   to png with a Python function. That function also pre-processes the image to maximize tesseract
   readability.
"""

import os
import subprocess
import sys
import cv2
import numpy as np

# run powershell script, pdf_to_tiff
p = subprocess.Popen(["powershell.exe",
                      "C:\\Users\\plog1\\Documents\\Scripts\\CNAmeters\\pdf_to_tiff.ps1"],
                     stdout=sys.stdout)
p.communicate()

def tiff_png(img_path):
    """Takes a raw tiff image, processes it, and saves it as a png file ready to be analyzed.

    Arguments:
        img_path {file path 'string'} -- This is the tiff file produced from the powershell script.
    """

    # read image using opencv
    img = cv2.imread(img_path)

    # extract the file name without the file extension
    file_name = os.path.basename(img_path).split('.')[0]
    file_name = file_name.split()[0]

    # create a directory for outputs
    output_path = 'cleaned_images\\'
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ### NOISE REMOVAL
    # convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    # Apply blur to smooth out the edges
    img = cv2.GaussianBlur(img, (5, 5), 0)

    ### BINARIZATION
    # apply threshold to get image with only b&w
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # save the filtered image in the output directory
    save_path = os.path.join(output_path, file_name + ".png")
    cv2.imwrite(save_path, img)
    os.remove(img_path)

for f in os.listdir('cleaned_images'):
    tiff_png(f'C:\\Users\\plog1\\Documents\\Scripts\\CNAmeters\\cleaned_images\\{f}')
