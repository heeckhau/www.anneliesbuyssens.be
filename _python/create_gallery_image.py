__author__ = 'heeckhau'

import sys
from PIL import Image

#create gallery image from input

def create_gallery_image(input_image, gallery_thumbnail_path):
    background = Image.open("images/others/stack_200_16.png")
    moz = Image.open(input_image)

    # 16 + 168 + 16

    sq_size = min(moz.size)
    box_x = (moz.size[0]-sq_size)/2
    box_y = (moz.size[1]-sq_size)/2
    sq_box = (box_x, box_y, box_x + sq_size, box_y + sq_size)

    square_moz = moz.crop(sq_box)
    #square_moz.save("tmp1.png")

    resize_moz = square_moz.resize((168,168))
    #resize_moz.save("tmp2.png")

    box = (16, 16, 16 + 168, 16 + 168)

    background.paste(resize_moz, box)

    new_file = gallery_thumbnail_path
    print(new_file)

    background.save(new_file)

if __name__ == "__main__":
    input_image = sys.argv[1]
    if not os.path.isfile(input_image):
        raise "Incorrect input"

    create_gallery_image(input_image)



