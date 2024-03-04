import cv2
import os
import numpy as np

def resize(image, def_size=300):
    in_width = image.shape[1]
    in_height = image.shape[0]

    ratio = def_size/in_width
    out_width = in_width * ratio
    out_height = in_height * ratio

    result = (int(out_width), int(out_height))
    return result

width = 600
height = 300
cols = 3
rows = 2
hor_marg = 40
vert_marg = 20

images = os.listdir("./imggrid/")

for file in images:
    impath = f"./imggrid/{file}"
    img = cv2.imread(impath)
    resize_img = cv2.resize(img, (width, height))
    cv2.imwrite(impath, resize_img)

blank_image_width = (vert_marg*(cols+1)) + width*cols
blank_image_height = (hor_marg*(rows+1)) + height*rows

canvas = np.zeros((blank_image_height, blank_image_width, 3), np.uint8)

positions = [(x,y) for x in range(cols) for y in range(rows)]

for (pos_x, pos_y),img in zip(positions, images):
    x = pos_x * (width + vert_marg) + vert_marg
    y = pos_y * (height + hor_marg) + hor_marg
    impath = f"./imggrid/{img}"
    image = cv2.imread(impath)
    canvas[y:y+height, x:x+width] = image

cv2.imwrite("canvas.jpg", canvas)




