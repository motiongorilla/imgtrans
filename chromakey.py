import cv2
import matplotlib.pyplot as plt
import numpy as np

foreground = "./chromakey/IMG-20191101-WA0002.jpg"
# foreground = "./chromakey/eng.jpg"
background = "./chromakey/bg.jpg"

fgimage = cv2.imread(foreground)
bgimage = cv2.imread(background)


dsize = (fgimage.shape[1], fgimage.shape[0])
resizedBG = cv2.resize(bgimage,dsize)

"""Naive approach"""
chroma = [40, 140, 0]
for i in range(fgimage.shape[1]):
    for j in range(fgimage.shape[0]):
        pixel = fgimage[j, i]
        if np.any(pixel == chroma):
            fgimage[j,i] = resizedBG[j,i]


cv2.imwrite("./chromakey/naiveresult.jpg", fgimage)

"""NumPy approach"""
# lower_green = np.array([0, 100, 0])
# upper_green = np.array([100, 255, 110])
"""Uniform color. Soldier example"""
# uniform_chroma = np.array([213, 183, 157])

# image_copy = np.copy(fgimage)
# image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
# mask = cv2.inRange(image_copy, lower_green, upper_green)
"""Uniform color. Soldier example"""
# mask = cv2.inRange(image_copy, uniform_chroma, uniform_chroma)

# masked_image = np.copy(image_copy)
# masked_image[mask != 0] = [0,0,0]

# copy_bg = np.copy(resizedBG)
# copy_bg = cv2.cvtColor(copy_bg, cv2.COLOR_BGR2RGB)
# copy_bg[mask == 0] = [0,0,0]

# finalimage = np.add(copy_bg, masked_image)
# finalimage = cv2.cvtColor(finalimage, cv2.COLOR_RGB2BGR)
# cv2.imwrite("./chromakey/greenscreencomp.jpg", finalimage)
# plt.imshow(finalimage)
# plt.show()
