from PIL import Image, ImageFilter


img = Image.open(r'.\Image Processing\pokemon\imgs\pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.BoxBlur(radius=3))

filtered_img.save(r".\Image Processing\pokemon\processed\blur.png", 'png')
filtered_img2.save(r"Image Processing\pokemon\processed\boxblur.png", 'png')
