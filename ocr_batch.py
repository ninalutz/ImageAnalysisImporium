"""
Script authored by Wilson Chen for Winter 24 DRG
"""

import easyocr
import shutil
import os
import random
import cv2
import numpy as np

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