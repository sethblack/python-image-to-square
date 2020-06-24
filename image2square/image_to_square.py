import sys

from PIL import Image
from PIL import ImageFilter

def image_to_square(in_file_name, out_file_name, width=0):
    original_image = Image.open(in_file_name)

    image_width, image_height = original_image.size

    max_edge = max(image_width, image_height)

    blurry_image = original_image.resize((max_edge, max_edge))
    blurry_image = blurry_image.filter(ImageFilter.GaussianBlur(radius=50))

    final_image = Image.new('RGB', (max_edge, max_edge))
    final_image.paste(blurry_image, (0,0))

    if image_width < image_height:
        final_image.paste(original_image, ((max_edge // 2) - (image_width // 2), 0))
    else:
        final_image.paste(original_image, (0, (max_edge // 2) - (image_width // 2)))

    if width > 0:
        final_image = final_image.resize((width, width))

    final_image.save(out_file_name)
