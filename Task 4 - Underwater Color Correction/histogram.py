import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('underWaterImg1.jpg', 0)

# compute histogram of original image
hist, bins = np.histogram(img.flatten(), 256, [0, 256])

# calculate accumulative sum of values as equation
# generate normalized histogram (equalized) equation
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max() / cdf.max()

plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

equ = cv2.equalizeHist(img)
cv2.imshow('equalized img', equ)

cv2.waitKey(0)
cv2.destroyAllWindows()



