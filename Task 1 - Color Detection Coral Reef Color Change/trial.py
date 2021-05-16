import cv2
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from skimage import data
from skimage.filters import threshold_multiotsu

original= cv2.imread("original.png",0)
img = original.copy()

mask = np.zeros(img.shape, img.dtype)
alpha =3.0
beta =0

#img = cv2.addWeighted(img, alpha, mask,0,beta)
img = cv2.equalizeHist(img)
cv2.imshow("hjk",img)
# finding appropriate thresholdings:
thresholds = threshold_multiotsu(img, 4)
print(thresholds)
thresh1 = thresholds[0]
thresh2 = thresholds[1]
thresh3 = thresholds[2]
x = img.shape[1]
y = img.shape[0]

for i in range (0,x):
    for j in range (0,y):
        if img[j,i] < thresh2 & img[j,i]>thresh1:
            img[j,i] = 100
        elif img[j,i]<thresh3 & img[j,i] >thresh2:
            img[j,i] = 160
        elif img[j,i]> thresh3:
            img[j,i] = 255
        else:
            img[j,i] =0



cv2.imshow("fghj",original)
cv2.imshow("fg",img)

cv2.imwrite("grayscale.jpg", original)


cv2.waitKey(0)
cv2.destroyAllWindows()

