import cv2
import numpy as np

img = cv2.imread('original.png')
ch_img = cv2.imread("change.png")
#res = cv2.resize(img, (0, 0), fx =1, fy= 1, interpolation = cv2.INTER_CUBIC) 

boundaries = [
    ([137,73,163], [177,113,203] ),
    ([ 220, 204, 182], [255, 244, 222])]

# save boundaries in a variable to use
# step mlhash ay 30 lazma l 72i2a
for (lower, upper) in boundaries:
    # must be of uint8 for the bitwise operation to work
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    # create mask to detect the required color
    # mask is created through detecting the range of colors within the boundaries leaving the others black
    O_mask = cv2.inRange(img, lower, upper)   # mask result is binary output( black and white)
    O_res = cv2.bitwise_and(img, img, mask = O_mask)     # mask result is the required color and black

    CH_mask = cv2.inRange(ch_img, lower, upper) 
    CH_res = cv2.bitwise_and(ch_img, ch_img, mask = CH_mask) 

    cv2.imshow('original', np.hstack([img, O_res]))
    cv2.imshow('changed', np.hstack([ch_img, CH_res]))
    
    cv2.waitKey(0)
    
cv2.destroyAllWindows()
