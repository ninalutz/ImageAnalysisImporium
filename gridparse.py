""""
This is a helper script written by Nina Lutz 
for parsing individual images in a grid formation from 
a composite image 
"""

import cv2

# Number of columns in the piece to chop
W_SIZE  = 5

# Number of rows in the piece to chop
H_SIZE = 10

#input file to chop
input_file = 'test_images/chop_test.png'

#type of output chopped images you want to save 
output_extension = ".jpg"

def chop_images(filename):
      directory = "test_images/grids/" #output directory

      img = cv2.imread(filename)
      img2 = img

      height, width, channels = img.shape
      counter = 0

      for ih in range(H_SIZE ):
         for iw in range(W_SIZE ):
         
            x = width/W_SIZE * iw 
            y = height/H_SIZE * ih
            h = (height / H_SIZE)
            w = (width / W_SIZE )
            counter+=1
            img = img[int(y):int(y+h), int(x):int(x+w)]
            cv2.imwrite(directory  + "grid_" + str(counter) + output_extension, img)
            img = img2

chop_images(input_file)



