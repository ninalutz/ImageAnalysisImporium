"""
Authored by Zayna Lughod 
This displays edges for an image 
Can be adopted for batch images too 
"""

import cv2
input_image = 'test_images/test_collection_fish/fish1.jpg'

img = cv2.imread(input_image)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)

# Display Sobel Edge Detection Images
cv2.imshow('edges1', sobelx)
cv2.imshow('edges2', sobely)
cv2.imshow('edges3', sobelxy)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

# Display Canny Edge Detection Image -- PRIMARY one for use
cv2.imshow('edges', edges)

cv2.waitKey(0) 



