import cv2
from skimage.measure import compare_ssim
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as imgs
import imutils

Original = cv2.imread('origin_2.jpg')
Changed = cv2.imread('aligned.jpg')

# changed = cv2.resize(changed, (original.shape[1], original.shape[0]), interpolation=cv2.INTER_CUBIC)
#original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
#changed_gray = cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)

lower_gray = np.array([25, 25, 25], dtype = "uint8")
upper_gray = np.array([151, 151, 151], dtype = "uint8")
upper_gray_2 = np.array([185, 185, 185], dtype = "uint8")

mask_1 = cv2.inRange(Original, lower_gray, upper_gray)
mask_2 = cv2.inRange(Changed, lower_gray, upper_gray_2)

# remove the background from the image

masked_image_1 = np.copy(Original)
masked_image_2 = np.copy(Changed)
masked_image_1[mask_1 != 0] = [0, 0, 0]
masked_image_2[mask_2 != 0] = [0, 0, 0]


green = cv2.subtract(masked_image_1, masked_image_2)

lower_green = np.array([0, 20, 30])
upper_green = np.array([0, 100, 100])

# convert the color to grayscale kont bgrab 7aga :D
original_gray = cv2.cvtColor(Original, cv2.COLOR_BGR2GRAY)
changed_gray = cv2.cvtColor(Changed, cv2.COLOR_BGR2GRAY)

# threshold byen mask1 wa mask2

h, thresh = cv2.threshold(cv2.subtract(mask_1, mask_2), 200, 255, cv2.THRESH_BINARY)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    # compute the bounding box of the contour and then draw
    # bounding box on both input images to represent where the two

    c = max(cnts, key=cv2.contourArea)
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(Original, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.rectangle(Changed, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow("original", np.hstack([Original, Changed]))

cv2.waitKey(0)
