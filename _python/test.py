__author__ = 'heeckhau'

import sys
from PIL import Image
import os

#create gallery image from input

def create_gallery_image(input_image):
    background = Image.open("images/others/stack_bg.png")
    moz = Image.open(input_image)

    # 50 + 450 + 50

    sq_size = min(moz.size)
    box_x = (moz.size[0]-sq_size)/2
    box_y = (moz.size[1]-sq_size)/2
    sq_box = (box_x, box_y, box_x + sq_size, box_y + sq_size)

    square_moz = moz.crop(sq_box)
    #square_moz.save("tmp1.png")

    resize_moz = square_moz.resize((450,450))
    #resize_moz.save("tmp2.png")

    box = (50, 50, 500, 500)

    background.paste(resize_moz, box)

    new_file = os.path.dirname(input_image) + "/gallery.png"
    print(new_file)

    background.resize((sq_size,sq_size)).save(new_file)

if __name__ == "__main__":
    input_image = sys.argv[1]
    if not os.path.isfile(input_image):
        raise "Incorrect input"

    create_gallery_image(input_image)



