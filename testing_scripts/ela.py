from PIL import Image, ImageChops, ImageEnhance
 
def calculate_ela(original_image_path, temp_image_path, scale_factor=10):
    # open original image
    original_image = Image.open(original_image_path)

    original_image.save(temp_image_path, quality=95)

    temp_image = Image.open(temp_image_path)

    #caculate the diff of the original image and temp
    ela_image = ImageChops.difference(original_image, temp_image)

    #calculate the scale factor (this from stack overflow and another git notebook)
    extrema = ela_image.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    if max_diff == 0:
        max_diff = 1
    scale = 255.0 / max_diff

    # adjust the pixels
    ela_image = ImageEnhance.Brightness(ela_image).enhance(scale_factor / scale)

    return ela_image

original_image_path = "test_images/"
original_image_path+= "10.png"
temp_image_path = 'tempImage.jpg'

ela_image = calculate_ela(original_image_path, temp_image_path)
ela_image.show()
