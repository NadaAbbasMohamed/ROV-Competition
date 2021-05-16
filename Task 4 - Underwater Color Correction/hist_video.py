import cv2

cap = cv2.VideoCapture('Tuna tornado.mp4')
#path = r'C:\Users\nada\Desktop\color correction\hist_video.mkv'
#VideoFileOutput = cv2.VideoWriter(path, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), 25, (640, 480))
while cap.isOpened():

    ret, frame = cap.read()
    scaled_frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)

    r, g, b = cv2.split(scaled_frame)
    hist_r = cv2.equalizeHist(r)
    hist_g = cv2.equalizeHist(g)
    hist_b = cv2.equalizeHist(b)

    hist_frame = cv2.merge((hist_r, hist_g, hist_b))
#   VideoFileOutput.write(hist_frame)
    cv2.imshow('result video', hist_frame)

    if cv2.waitKey(10) == 25:
        break
cap.release()
cv2.destroyAllWindows()
