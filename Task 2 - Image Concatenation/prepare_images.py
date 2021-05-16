import cv2
import glob

cap = cv2.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    X = frame.shape[1]/2
    Y = frame.shape[0]/2
    x = 50
    y = 100
    h = frame.shape[0]-200
    w = frame.shape[1]-100
    frame = cv2.rectangle(frame, (x,y), (x+w, y+h), color=(0, 255,0), thickness=int(2))
    frame = cv2.rectangle(frame, (int(X-200),int(Y-200)), (int(X+200), int(Y+200) ), color=(0, 0, 255), thickness=int(2))
    cv2.imshow('To Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

images = glob.glob('C:/Users/nada/Desktop/ROV Competition/task 3 - subway car/other imgs/*.jpg')
i = 0
for im in images:
    img = cv2.imread(im)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
    image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # find the biggest countour (c) by the area
    cnt = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(cnt)

    # draw the biggest contour (c) in green
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('res', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('fig_'+str(i)+'.jpg', img[y:y+h, x:x+w])
    #cv2.imwrite('C:/Users/nada/Desktop/ROV Competition/task 3 - subway car/' + )

