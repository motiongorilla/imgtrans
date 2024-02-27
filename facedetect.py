import cv2
from pathlib import Path

file = "./imgs/faces_00.jpg"
face_cascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")
red = (0, 255, 0)

dir = Path("./imgs/")
new_dir = "./imgs/detected/"
if not Path(new_dir).exists():
    Path(new_dir).mkdir()

for file in dir.iterdir():
    if file.stem.__contains__("face"):
        img = cv2.imread(file.__str__(), 1)
        faces = face_cascade.detectMultiScale(img, 1.15, 8)

        for (x,y,w,h) in faces:
            start = (x, y)
            end = (x+w, y+h)
            cv2.rectangle(img, start, end, color=red, thickness=10)

        oldname = file.stem
        format = file.suffix
        newname = f"{new_dir}/detected_{oldname}{format}"
        cv2.imwrite(newname.__str__(), img)
