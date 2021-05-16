import cv2
import numpy as np
import matplotlib.pyplot as plt

def hist(im):
    rows, columns = im.shape
    intensity_levels = 2 ** 8
    freq = [0]*intensity_levels
    # collecting frequency of color intensities used
    # collecting image Histogram
    for i in range(rows):                          # rows
        for j in range(columns):                     # columns
            for k in range(intensity_levels):       # intensity_levels
                if r[i, j] == k:
                    freq[k] = freq[k]+1
                    break
                else:
                    k = k+1
            j = j+1
            if j == columns:
                break
        i = i+1
        if i == rows:
            break
    bins = list(range(0, intensity_levels))
    plt.rcParams["figure.figsize"] = (3, 3)
    fig, ax = plt.subplots()
    ax.plot(bins, freq)
    plt.show()

    eq_hist = [0]*intensity_levels
    com_sum = 0

    for i in range(intensity_levels):
        com_sum = freq[i] + com_sum
        eq_hist[i] = 256*com_sum

    sk = np.uint8(255*eq_hist)
    y = np.zeros_like(r)

    for i in range(rows):
        for j in range(columns):
            y[i, j] = sk[r[i, j]]

    plt.imshow(y)
    plt.show()

img = cv2.imread('pool5.jpg')
r, g, b = cv2.split(img)
hist(r)
# bit_depth = r.dtype  # color intensity levels
# specify bit depth of image later according to equivalent bit number
# 8unty form list take element num 0

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
