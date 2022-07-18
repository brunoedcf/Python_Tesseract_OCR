import numpy as np
import pytesseract
import time
import cv2
import os

from pdf2image import convert_from_path

# Calculate processing time
start_time = time.time()

# Your file path goes here
file_path = "YOUR_FILE_PATH"

# Get file extension
split_extension = os.path.splitext(file_path)
file_extension = split_extension[1]

if file_extension == '.pdf':
    # One page for each index of the array
    text = []

    # Use pdf2image to convert every page from the pdf to an image
    pages = convert_from_path(file_path)

    # Iterate all pages
    for i in range(len(pages)):

                # Uses numpy and cv2 to normalize the image and help the OCR
                my_image = np.array(pages[i])
                norm_img = np.zeros((my_image.shape[0], my_image.shape[1]))
                my_image = cv2.normalize(my_image, norm_img, 0, 255, cv2.NORM_MINMAX)
                my_image = cv2.threshold(my_image, 100, 255, cv2.THRESH_BINARY)[1]
                my_image = cv2.GaussianBlur(my_image, (1, 1), 0)

                # Here pytesseract extracts the image with the Portuguese lang loaded
                my_text = pytesseract.image_to_string(my_image, lang='por')

           
# Print total processing time
print("Total time: " + str( int(time.time() - start_time) ) + " seconds.")