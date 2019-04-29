"""
   DOCSTRING
"""

import os
import cv2
import pytesseract

# Define config parameters
# config = '-l eng --oem 2 --psm 3'

def write_files(img):
    im = cv2.imread(f'C:\\Users\\plog1\\Documents\\Scripts\\CNAmeters\\cleaned_images\\{img}',
                    cv2.IMREAD_COLOR)
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im) #, config=config)
    # trims file name
    img = os.path.splitext(img)[0]
    # Prints output
    with open(f'outputs\\{img}.txt', 'w') as out:
        out.write(text)

for f in os.listdir('cleaned_images'):
    write_files(f)
