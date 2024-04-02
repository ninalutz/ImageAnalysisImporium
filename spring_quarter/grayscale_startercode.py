import glob
import sys
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os

#add input and output folders
input_folder_name = "test_images/test_collection"
output_folder_name = "test_images/test_collection/grayed"


def adjust_images(input_images, output_folder_name):
  assert len(input_images) >= 1, "No images found in the directory"
  # Determine the largest dimensions in the set of images
  max_width, max_height = find_largest_image_size(input_images)

  # Since each image might have different dimensions, resize all images
  # to the maximum dimensions and center them before averaging
  for image_path in input_images:
    #THIS IS WHERE WE WANT TO CONVERT TO GRAYSCALE

  return glob.glob(output_folder_name + '/*.png')
