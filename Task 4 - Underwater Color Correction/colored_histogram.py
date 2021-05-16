import cv2
img = cv2.imread('underWaterImg1.jpg', 1)
cv2.imshow('original', img)
r, g, b = cv2.split(img)

hist_r = cv2.equalizeHist(r)
hist_g = cv2.equalizeHist(g)
hist_b = cv2.equalizeHist(b)

hist_img = cv2.merge((hist_r, hist_g, hist_b))

scale = 1
rows = int(hist_img.shape[1]*scale)
columns = int(hist_img.shape[0]*scale)

#scaled_img = cv2.resize(hist_img, (rows, columns), interpolation=cv2.INTER_AREA)

cv2.imshow('equalized img', hist_img)
#cv2.imshow('interpolated img', scaled_img)

#cv2.imwrite('equalized img.jpg', hist_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
