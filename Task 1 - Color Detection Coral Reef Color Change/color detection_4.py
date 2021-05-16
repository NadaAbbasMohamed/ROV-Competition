import cv2
import numpy as np

def color_detect(img, lower_bound, upper_bound):
    lower_bound = np.array(lower_bound, dtype = "uint8")
    upper_bound = np.array(upper_bound, dtype = "uint8")

    mask = cv2.inRange(img, lower_bound, upper_bound)
    res = cv2.bitwise_and(img, img, mask = mask)
    #return res
    return mask

Original = cv2.imread("original.png")
Changed = cv2.imread("changed.png")

Original = cv2.resize(Original, (0, 0), fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)

original = cv2.GaussianBlur(src = Original, ksize = (5, 5), sigmaX = 0)
changed = cv2.GaussianBlur(src = Changed, ksize = (5, 5), sigmaX = 0)

P_lowerBoundary = [137, 73, 163]
P_upperBoundary = [177, 113, 203]

W_lowerBoundary = [220, 204, 182]
W_upperBoundary = [255, 244, 222]

O_P_res = color_detect(original, P_lowerBoundary, P_upperBoundary)
O_W_res = color_detect(original, W_lowerBoundary, W_upperBoundary)

CH_P_res = color_detect(changed, P_lowerBoundary, P_upperBoundary)
CH_W_res = color_detect(changed, W_lowerBoundary, W_upperBoundary)

contours, hierarchy = cv2.findContours(O_P_res, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

epsilon = 0.1*cv2.arcLength(contours, slice=cv2.WHOLE_SEQ, isClosed=-1)
approx = cv2.approxPolyDP(contours,epsilon,True)

cv2.drawContours(Original, contours, -1, (255, 0, 0), 2)

i = 1
for c in contours:
    area = cv2.contourArea(c)

    if area > 50:
        (x, y, w, h) = cv2.boundingRect(c)

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(Original, [box], 0, (0, 0, 255), 2)


cv2.imshow(' Original Pink extraction result', Original)
cv2.waitKey(0)
cv2.destroyAllWindows()

