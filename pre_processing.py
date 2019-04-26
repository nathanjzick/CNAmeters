"""[The preprocessing of an image file along with the saving of the file.]

Returns:
    [Saved file] -- [Processed image file]
"""

import os
import cv2
import numpy as np

def do_work(img_path):
    """[Takes a raw image, processes it, and saves it to a output path called cleaned_images]

    Arguments:
        img_path {[file path 'string']} -- [This is the original image that will be processed]
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

do_work('C:\\Users\\plog1\\Documents\\Scripts\\CNAmeters\\file.tiff')
