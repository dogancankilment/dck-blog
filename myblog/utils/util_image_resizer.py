import PIL
from PIL import Image
from celery import shared_task


@shared_task
def image_resizer(path):
    basewidth = 300
    img = Image.open(path)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
    img.save(path)
