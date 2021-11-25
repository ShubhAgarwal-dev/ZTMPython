from PIL import Image

img = Image.open(r'Image Processing\resizing\astro.jpg')
img.thumbnail((400, 400))
# thumbnail does not return a image but modify one and keeps the aspect ratio same
img.save(r'Image Processing\resizing\thumbnail.jpg')
