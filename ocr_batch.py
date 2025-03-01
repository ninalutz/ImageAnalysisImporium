<<<<<<< Updated upstream
"""
Script authored by Wilson Chen for Winter 24 DRG
Edits by Nina Lutz 

This script uses easyocr to extract text from images,
with some modifications for better extraction 

It extracts into separate text files for each image 
and an overall output CSV
"""

import easyocr
import shutil
import os
import random
import cv2
import numpy as np
import glob
import sys
import csv

try:
  from PIL import Image
except ImportError:
  import Image


# Helper methods for preprocessing images - these might increase OCR accuracy. Use as needed.
# Code attributions go to https://nanonets.com/blog/ocr-with-tesseract/
is_grayscale = False


def get_grayscale(image):
  is_grayscale = True
  return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
  return cv2.medianBlur(image, 5)

def thresholding(image):
  return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def gaussian_thresholding(image):
  # from https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html
  th3 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
  return th3

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)

#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    is_grayscale = True
    return cv2.Canny(image, 100, 200)

def main():
    print('testing main method for ocr')
    input_folder_name = "test_images/test_collection_memes"
    output_folder_name = "output/meme_ocr"
    output_name = "memes_text"

    uploads = glob.glob(input_folder_name + '/*.*')

    output_filename_txt = output_name + ".txt"

    contents_output_txt = ""

    csv_dict = {}


    for upload in uploads:
      print("Processing: " + str(upload))

      img = cv2.imread(upload);
      img_processed = img

      # ## Image processing


      # Apply grayscale
      img_processed = get_grayscale(img_processed)

      # Run gaussian thresholding
      # img_processed = gaussian_thresholding(img_processed)

      # # Apply noise removal
      # img_processed = remove_noise(img_processed)

      reader = easyocr.Reader(['en'])
      output = reader.readtext(img_processed)


      # Draw bounding boxes
      for bbox, text, confidence in output:
          bbox = np.array(bbox, dtype=np.int32)
          cv2.polylines(img_processed, [bbox], isClosed=True, color=(128, 128, 128), thickness=2)
          # Optional: adds the detected text by the bounding box.
          # cv2.putText(img_processed, f'{text}: {confidence:.2f}', (bbox[0][0], bbox[0][1] - 10),
          #             cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

      # Display the result
      # cv2.imshow('img', img_processed)
      # cv2.waitKey(0)

      # Upload the text to a .txt file with the image's name
      last_dot_index = upload.rfind('.')
      filename_without_extension = upload[:last_dot_index].split('/')[-1]
      filename_txt = output_folder_name + '/' + filename_without_extension + ".txt"
      print(f'filename: {filename_txt}')

      this_text = ""
      with open(filename_txt, 'w', encoding='utf-8') as file:
          for _, text, _ in output:
            file.write(text + '\n')
            this_text += text + '\\n'

      csv_dict[filename_without_extension] = this_text

      print("-----")
      print("Text extracted from the image has been saved to:", filename_txt)

    print("Processed images, writing to CSV")

    with open('output.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        for k in csv_dict:
            csvwriter.writerow([k, csv_dict[k]])
            
if __name__ == '__main__':
    main()

=======
>>>>>>> Stashed changes
