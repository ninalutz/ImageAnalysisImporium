"""
Authored by Zayna Lughod 
This displays edges for an image 
Adopted for batching by Nina Lutz
"""

import cv2
import glob
import sys

input_folder_name = "test_images/test_collection_border"
output_directory = "test_images/test_collection_border/edges"
uploads = glob.glob(input_folder_name + '/*.*')


for input_image in uploads:
	print("proccessing: " + input_image)
	img = cv2.imread(input_image)
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
	edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

	cv2.imwrite('test_images/test_collection_border/edges/' + input_image.split('/')[2], edges) 
