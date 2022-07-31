from PIL import Image
import os

def changePixels(imagePath, index):
    image = Image.open(imagePath, 'r')
    pixels = list(image.getdata())
        
    newPixels = []
    for pixel in pixels:
        newPixel = (pixel[1], pixel[1], pixel[2]) # G G B
        newPixels.append(newPixel)

    newImage = Image.new(image.mode, image.size)
    newImage.putdata(newPixels)
    newImage.save(f"newImages/newImg-{index}.png")
    print("Done")

images = os.listdir("images/")
imagePaths = []
index = 0
for image in images:
    imagePath = f"images/{image}"
    changePixels(imagePath, index)
    index += 1