import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread("original.png")
blue = original.copy()
green = original.copy()
red = original.copy()

blue[:, :, 2] = 0
blue[:, :, 1] = 0

green[:, :, 0] = 0
green[:, :, 2] = 0

red[:, :, 0] = 0
red[:, :, 1] = 0

B_hist = cv2.calcHist([blue], [0], None, [256], [0, 255])
#plt.figure()
#plt.title(" Blue Histogram")
#plt.plot(B_hist)
#plt.xlim([0,255])
#plt.show()
#cv2.waitKey(0)

G_hist = cv2.calcHist([green], [0], None, [256], [0, 255])
#plt.figure()
#plt.title(" Green Histogram")
#plt.plot(G_hist)
#plt.xlim([0,255])
#plt.show()
#cv2.waitKey(0)

R_hist = cv2.calcHist([red], [0], None, [256], [0, 255])
#plt.figure()
#plt.title(" Red Histogram")
#plt.plot(R_hist)
#plt.xlim([0,255])
#plt.show()
#cv2.waitKey(0) 

original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
hist = cv2.calcHist([original], [0], None, [256], [0, 255])
plt.figure()
plt.title(" grayscale Histogram")
plt.plot(hist)
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)

cv2.imshow("blue", blue)
cv2.imshow("green", green)
cv2.imshow("red", red)
cv2.imshow("original", original)

cv2.waitKey(0)
cv2.destroyAllWindows()
