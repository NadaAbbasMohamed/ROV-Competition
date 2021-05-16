import cv2
import numpy as np

Original = cv2.imread("original.png")
Changed = cv2.imread("change.png")
# specify colors boundaries
P_lowerBoundary = [137, 73, 163]
P_upperBoundary = [177, 113, 203]

W_lowerBoundary = [220, 204, 182]
W_upperBoundary = [255, 244, 222]

# change data type to uint8 to be used with the bitwise_and function
P_lowerBoundary = np.array(P_lowerBoundary, dtype = "uint8")
P_upperBoundary = np.array(P_upperBoundary, dtype = "uint8")

W_lowerBoundary = np.array(W_lowerBoundary, dtype = "uint8")
W_upperBoundary = np.array(W_upperBoundary, dtype = "uint8")

# Create Color Mask
P_mask = cv2.inRange(Original, P_lowerBoundary, P_upperBoundary) 
W_mask = cv2.inRange(Original, W_lowerBoundary, W_upperBoundary)

# Merge detected color with mask
P_res = cv2.bitwise_and(Original, Original, mask = P_mask)
W_res = cv2.bitwise_and(Original, Original, mask = W_mask)

cv2.imshow('PINK', np.hstack([Original, P_res]))
cv2.imshow('White', np.hstack([Original, W_res]))

cv2.waitKey(0)
cv2.destroyAllWindows()
