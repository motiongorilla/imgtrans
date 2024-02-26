import cv2
from pathlib import Path

file = "./image_00.jpg"
# color = cv2.imread(file, 0)

dir = Path("./imgs/")
for file in dir.iterdir():
    color_data = cv2.imread(file.__str__(), 0)
    oldname = file.stem
    fileformat = file.suffix
    newname = str(file.with_name(f"{oldname}_GS{fileformat}"))
    cv2.imwrite(newname, color_data)

