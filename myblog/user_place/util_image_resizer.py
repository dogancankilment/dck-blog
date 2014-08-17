# image
import PIL
from PIL import Image


def image_resizer():
    basewidth = 300
    img = Image.open('deneme.jpg')
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save('resized_image.jpg')