import math
import cv2
from pathlib import Path

dir = Path("./imgs/")

def uniform_scale(scale_percentage, width, height) -> tuple:
    new_width = (width * scale_percentage) / 100
    new_height = (height * scale_percentage) / 100

    return (int(new_width), int(new_height))

def resize_to_power_of_two(width, height):
    width_closest_power = round(math.log2(width))
    height_closest_power = round(math.log2(height))
    new_width = pow(2, width_closest_power)
    new_height = pow(2, height_closest_power)
    width_ratio = new_width/width
    height_ratio = new_height/height

    return (new_width, new_height,(width_ratio, height_ratio))

# resize_nums = resize_to_power_of_two(img.shape[1], img.shape[0])

def resize_img(image_path, out_path,scale_percent=50, uniform: bool = False, power_of_two: bool = False, width_based_power_two: bool = False, height_based_power_two: bool = False):
    imgread = cv2.imread(image_path)
    new_dsize = (imgread.shape[1], imgread.shape[0])
    if uniform and power_of_two == False:
        power_of_two = False
        width_based_power_two = False
        height_based_power_two = False
        new_dsize = uniform_scale(scale_percent, imgread.shape[1], imgread.shape[0])

    if power_of_two and uniform == False:
        uniform = False
        new_dimensons = resize_to_power_of_two(imgread.shape[1], imgread.shape[0])
        width = new_dimensons[0]
        height = new_dimensons[1]
        if width_based_power_two:
            height_based_power_two = False
            height = imgread.shape[0] * new_dimensons[2][0]

        if height_based_power_two:
            width_based_power_two = False
            width = imgread.shape[1] * new_dimensons[2][1]
        new_dsize = (int(width), int(height))

    print(new_dsize[0], new_dsize[1])
    resized_img = cv2.resize(imgread, new_dsize)
    cv2.imwrite(out_path, resized_img)

for file in dir.iterdir():
    oldname = file.stem
    format = file.suffix
    newpath = file.with_name(f"{oldname}_resized{format}")
    resize_img(file.__str__(), newpath.__str__(), power_of_two=True)

