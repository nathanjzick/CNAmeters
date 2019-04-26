import pytesseract

# Recognize text with tesseract for python
    result = pytesseract.image_to_string(img, lang="eng")
    return result