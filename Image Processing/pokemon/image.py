from PIL import Image, ImageFilter


img = Image.open(r'.\Image Processing\pokemon\imgs\pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img2 = img.filter(ImageFilter.BoxBlur(radius=1.9))

filtered_img.save(r".\Image Processing\pokemon\processed\blur.png", 'png')
filtered_img2.save(r"Image Processing\pokemon\processed\boxblur.png", 'png')
filtered_img3 = filtered_img2.rotate(angle=90.0)
filtered_img3.save(r"Image Processing\pokemon\processed\rotate.png", 'png')
