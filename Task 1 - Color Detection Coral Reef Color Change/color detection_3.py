import cv2
import numpy as np

def color_detect(img, lower_bound, upper_bound):
    lower_bound = np.array(lower_bound, dtype = "uint8")
    upper_bound = np.array(upper_bound, dtype = "uint8")

    mask = cv2.inRange(img, lower_bound, upper_bound)
    res = cv2.bitwise_and(img, img, mask= mask)

    return res

orig = cv2.imread("original.png")
changed = cv2.imread("change.png")

# resizing important for subtraction (images must be of the same size)
changed = cv2.resize(changed, (orig.shape[1], orig.shape[0]), interpolation = cv2.INTER_CUBIC) 

orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
changed = cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)

original = cv2.equalizeHist(orig)
changed = cv2.equalizeHist(changed)


orig = cv2.cvtColor(orig, cv2.COLOR_GRAY2BGR)
changed = cv2.cvtColor(changed, cv2.COLOR_GRAY2BGR)


# blurring enhance the result of mask
# allignment and fitting of the 2 images must be achieved first - 3shan l result baiz 5als
original = cv2.GaussianBlur(src= original, ksize= (5, 5), sigmaX= 0)
changed = cv2.GaussianBlur(src= changed, ksize= (5, 5), sigmaX= 0)


P_lowerBoundary = [137, 73, 163]
P_upperBoundary = [177, 113, 203]

W_lowerBoundary = [220, 204, 182]
W_upperBoundary = [255, 244, 222]

O_P_res = color_detect(original, P_lowerBoundary, P_upperBoundary)
O_W_res = color_detect(original, W_lowerBoundary, W_upperBoundary)

CH_P_res = color_detect(changed, P_lowerBoundary, P_upperBoundary)
CH_W_res = color_detect(changed, W_lowerBoundary, W_upperBoundary)

#P_res = cv2.bitwise_xor(O_P_res, CH_P_res)
#P_res = O_P_res - CH_P_res
P_res = cv2.subtract(O_P_res, CH_P_res)
W_res = cv2.subtract(O_W_res, CH_W_res)

cv2.imshow('ORIGINAL', np.hstack([original, O_P_res, O_W_res]))
cv2.imshow('CHANGED', np.hstack([changed, CH_P_res, CH_W_res]))
cv2.imshow("pink subtraction result", P_res)
cv2.imshow("White subtraction result", W_res)

cv2.waitKey(0)
cv2.destroyAllWindows()
