from PIL import Image, ImageEnhance, ImageFilter
import os

p = " " # unedited
pathOut = " " # folder for edited images

from PIL import Image, ImageEnhance, ImageFilter
import os

# folder for unedited images
p = "D:\\downloads\\WhatsApp.jpg"
pathOut = "D:\\downloads" # folder for edited images

img = Image.open(p)

# sharpening, BW
edit = img.filter(ImageFilter.SHARPEN).convert('L')

# contrast
factor = 1.5
enhancer = ImageEnhance.Contrast(edit)
edit = enhancer.enhance(factor)

clean_name = os.path.splitext(os.path.basename(p))[0]

edit.save(f'{pathOut}/{clean_name}_edited.jpg')