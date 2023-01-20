from PIL import Image, ImageDraw, ImageFont
import os

filename = os.sys.argv[1]
im1 = Image.open(filename)

def resize_image(image_path):
    with Image.open(image_path) as image:
        width, height = image.size
        if width > height:
            ratio = 500 / width
            new_width = 500
            new_height = int(height * ratio)
        else:
            ratio = 500 / height
            new_width = int(width * ratio)
            new_height = 500

        resized_image = image.resize((new_width, new_height))
        return resized_image

def write_text(image, text):
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font = ImageFont.truetype("arial.ttf", 36)
    textwidth, textheight = draw.textsize(text, font=font)
    x = (width - textwidth) / 2
    y = (height - textheight) / 2
    draw.text((x, y), text, fill=(255, 0, 0), font=font)
    return image

im1 = resize_image(filename)

L,H=im1.size

treshold = int(os.sys.argv[2])

im2 = Image.new("RGBA",(L,H))
for y in range(H):
    for x in range(L):
        p = im1.getpixel((x,y))
        gris = int((p[0]+p[1]+p[2])//3)
        if gris > treshold:
            im2.putpixel((x,y),(0,0,0,0))
        else:
            im2.putpixel((x,y),(54,57,62,255))

im2 = write_text(im2, os.sys.argv[3])

chaine = "grey-"+filename
im2.save(chaine)