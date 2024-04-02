"""
Authored by Katie Arriaga in W24 DRG 
Small edit to support multiple inputs by Nina Lutz

Takes in a folder of images and outputs the average image
Via composite imagery 
"""
import glob
import sys
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import os

#add input and output folders for resizing
input_folder_name = "test_images/test_collection"
output_folder_name = "test_images/test_collection/resized"

# Function to find the largest dimensions of withing a set of images
def find_largest_image_size(image_files):
    # Open the first image to get its size
    first_image_path = os.path.join(image_files[0])
    first_img = Image.open(first_image_path)
    max_width, max_height = first_img.size

    # Loop through the remaining images and find the maximum size
    for image_file in image_files[1:]:
        img = Image.open(image_file)
        max_width = max(max_width, img.width)
        max_height = max(max_height, img.height)
    return max_width, max_height

# Function to resize an image to a given width and height
def resize_image(input_path, output_folder, width, height):
    # Open the image file
    original_image = Image.open(input_path)

    # Get the original image size
    original_width, original_height = original_image.size

    # Calculate the aspect ratio of the original image
    aspect_ratio = original_width / original_height

    # Calculate the new dimensions based on the provided width or height
    if height > width:
        new_width = width
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = height
        new_width = int(new_height * aspect_ratio)

    # Resize the image while maintaining the aspect ratio
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)

    # Create a new image with the desired dimensions and paste the resized content in the center
    result_image = Image.new("RGB", (width, height), (255, 255, 255))
    offset = ((width - new_width) // 2, (height - new_height) // 2)
    result_image.paste(resized_image, offset)

    # Check if a resulting directory exists and create it if not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get the filename of the original image to save it as such in the output folder
    original_filename = os.path.basename(input_path)
    output_path = output_folder + "/" + original_filename

    # Save the resulting image gile to the output path
    result_image.save(output_path)

def adjust_images(input_images, output_folder_name):
  assert len(input_images) >= 1, "No images found in the directory"
  # Determine the largest dimensions in the set of images
  max_width, max_height = find_largest_image_size(input_images)

  # Since each image might have different dimensions, resize all images
  # to the maximum dimensions and center them before averaging
  for image_path in input_images:
    resize_image(image_path, output_folder_name, max_width, max_height)

  return glob.glob(output_folder_name + '/*.png')

# Main routine

# Read the stream of all the images in the sample
input_images = glob.glob(input_folder_name + '/*.*')

# Adjust images before performing average
adjusted_images = adjust_images(input_images, output_folder_name)

# Initialize an empty list to store average image data
image_data = []

# Loop through each image file
for image in adjusted_images:
    # Read the image using OpenCV in color BGR
    cv_image = cv2.imread(image, cv2.IMREAD_COLOR)
    # Convert to RGB
    cv_image_rgb =  cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
    # Append the image data to the list
    image_data.append(cv_image_rgb)

assert len(image_data) >= 1, "No images found in the directory of adjusted images."

# Initialize the average image with the first image in the list
avg_image = image_data[0]

# Loop through each image in the list
for i in range(len(image_data)):
    # Skip the first image (i == 0) as it is already set as the average image
    if i == 0:
        pass
    else:
        # Calculate alpha and beta for weighted addition
        alpha = 1.0 / (i + 1)
        beta = 1.0 - alpha

        # Update the average image using weighted addition
        avg_image = cv2.addWeighted(image_data[i], alpha, avg_image, beta, 0.0)

# Save the averaged image to a PNG file
cv2.imwrite('average.png', avg_image)

# Read the averaged image from the saved file
avg_image = cv2.imread('average.png')

# Display the averaged image using Matplotlib
plt.imshow(avg_image)
plt.show()