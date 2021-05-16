import cv2
import numpy as np
from scipy.spatial import distance as dist

cap = cv2.VideoCapture(0)

while(cap):

    ret, frame = cap.read()
    PPI = 135.15       # number of pixels per inch
    # g_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    g_frame = cv2.GaussianBlur(src=frame, ksize=(5, 5), sigmaX=0)

    hsv_frame = cv2.cvtColor(g_frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([38, 86, 0])
    upper_blue = np.array([121, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # t , binary = cv2.threshold(g_frame, thresh = 150, maxval =255 , type = cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    pixelsPerMetric = None

    i = 1
    for c in contours:
        area = cv2.contourArea(c)

        if area > 1000:
            print("area is: ", area)
            (x, y, w, h) = cv2.boundingRect(c)

            # draw rectange with considering the rotation of object
            rect = cv2.minAreaRect(c)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

            height = str(i) + "- Height = " + str(h) + "    -     Width = " + str(w)
            cv2.putText(frame, height, (20, 15 + 15 * (i - 1)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0),
                        lineType=cv2.LINE_AA)
            i = i + 1

            ####################################################################################################
            # original code

            (tl, tr, br, bl) = box
            (tltrX, tltrY) = (tl[0] + tr[0]) / 2, (tl[1] + tr[1]) / 2
            (blbrX, blbrY) = (bl[0] + br[0]) / 2, (bl[1] + br[1]) / 2

            # compute the midpoint between the top-left and top-right points,
            # followed by the midpoint between the top-righ and bottom-right
            (tlblX, tlblY) = (tl[0] + bl[0]) / 2, (tl[1] + bl[1]) / 2
            (trbrX, trbrY) = (tr[0] + br[0]) / 2, (tr[1] + br[1]) / 2

            # draw the midpoints on the image
            cv2.circle(frame, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
            cv2.circle(frame, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
            cv2.circle(frame, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
            cv2.circle(frame, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

            # draw lines between the midpoints
            cv2.line(frame, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
            cv2.line(frame, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

            # dA = np.sqrt(sum([(tltrX - tltrY) ** 2 for tltrX, tltrY in zip(blbrX, blbrY)]))

            # compute the Euclidean distance between the midpoints
            dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
            dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

            dimA = dA / PPI
            dimB = dB / PPI
            cv2.putText(frame, "{:.1f}in".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
            cv2.putText(frame, "{:.1f}in".format(dimB), (int(trbrX + 10), int(trbrY)), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
        cv2.imshow("RESULT", frame)
        #cv2.imshow("Result 2", orig)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()