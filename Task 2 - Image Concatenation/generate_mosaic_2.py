import cv2 
import glob
import numpy as np 
from PIL import Image
from PIL import ImageFile

# Preparing images after capturing:
pathes = glob.glob('C:/Users/nada/Desktop/ROV Competition/task 3 - subway car/other imgs/*.jpg')
i = 0
sides = []
for path in pathes:
    img = cv2.imread(path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find the biggest countour (c) by the area
    cnt = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(cnt)
    
    # creating list for storing sides of subway car
    sides.append(img[y:y+h, x:x+w])

    # draw the biggest contour (c) in green
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('sides extraction from background result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #cv2.imwrite('fig_'+str(i)+'.jpg', img[y:y+h, x:x+w])

sq_sides = []
rec_sides = []
# to resize the side:
s_short = 125
s_long = s_short *2   # X size of rectangle = double X size of square

for side in sides:
    A = side.shape[1]   # the height of side 
    B = side.shape[0]   # the width of side
    C = abs(A-B) # the difference between length and width of the side 
    if C <= 10 and C>= 0:
        sq_sides.append(cv2.resize(side, (s_short, s_short), interpolation = cv2.INTER_CUBIC))
    elif C >= 50:
        rec_sides.append(cv2.resize(side, (s_long, s_short), interpolation = cv2.INTER_CUBIC))

# concatenating sides:
# stage 1 - concatenate horizontal bottom images:

horizontal_1 = cv2.hconcat([sq_sides[0], rec_sides[0], sq_sides[1], rec_sides[1]])
cv2.imshow('Horizontal Concatenate 1', horizontal_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# stage 2 - concatenate horizontal top images:
# to replace the filled sides with white background
white = cv2.imread('C:/Users/nada/Desktop/ROV Competition/task 3 - subway car/out.jpg')
bg_1 = cv2.resize(white, (s_long, s_short))     #create rectanglar shaped background 
bg_2 = cv2.resize(white, (s_short, s_short))    #create square shaped background

horizontal_2 = cv2.hconcat([bg_2, rec_sides[2], bg_2, bg_1])
cv2.imshow('Horizontal Concatenate 2', horizontal_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# stage 3 - concatenate vertical images:
vertical_res = cv2.vconcat([horizontal_2, horizontal_1])
#vertical_res = cv2.resize(vertical_res, (vertical_res.shape[1]*5, vertical_res.shape[0]*5), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Final Result', vertical_res)
cv2.waitKey(0)
cv2.destroyAllWindows()
