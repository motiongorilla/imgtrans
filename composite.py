import cv2

file = "./composite/meso.png"
wmfile = "./composite/site-logo.png"

img = cv2.imread(file)
watermark = cv2.imread(wmfile)

pos_x = img.shape[1] - watermark.shape[1]
pos_y = img.shape[0] - watermark.shape[0]

wm_place = img[pos_y:, pos_x:]
alpha = 0.5
beta = 1.0 - alpha
composed = cv2.addWeighted(wm_place, alpha, watermark, beta, 0)

img[pos_y:, pos_x:] = composed
cv2.imwrite("./wm.jpg", img)
