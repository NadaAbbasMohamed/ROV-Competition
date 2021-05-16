import cv2

img = cv2.imread('pool6.jpg')
cv2.imshow('original', img)
#step(1): bilateral Filtering for image smoothing
r, g, b = cv2.split(img)
r_filter = cv2.bilateralFilter(r, 10, 80, 30)
g_filter = cv2.bilateralFilter(g, 10, 80, 30)
b_filter = cv2.bilateralFilter(b, 10, 80, 30)
img_filtered = cv2.merge((r_filter, g_filter, b_filter))
cv2.imshow('filtered', img_filtered)
filtered = cv2.bilateralFilter(img, 10, 80, 30)
cv2.imshow('original', filtered)
# apply smoothing filter
# trial 1: bilateral filter
##median = cv2.medianBlur(hist_img, 5)

##median = cv2.edgePreservingFilter(hist_img, )
#interp_img = cv2.resize(median, (int(median.shape[1]*1), int(median.shape[0]*1)), interpolation=cv2.INTER_LINEAR)

#r, g, b = cv2.split(img)
#r_hist = cv2.equalizeHist(r)
#g_hist = cv2.equalizeHist(g)
#b_hist = cv2.equalizeHist(b)

#hist_img = cv2.merge((r_hist, g_hist, b_hist))

#cv2.imshow('trial', hist_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
