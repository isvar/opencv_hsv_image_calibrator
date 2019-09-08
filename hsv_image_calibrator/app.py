import cv2
import numpy as np


def nothing():
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow("trackbars")

# trackbars creation
cv2.createTrackbar("LH", 'trackbars', 0, 180, nothing)
cv2.createTrackbar("LS", 'trackbars', 0, 255, nothing)
cv2.createTrackbar("LV", 'trackbars', 0, 255, nothing)
cv2.createTrackbar("UH", 'trackbars', 0, 180, nothing)
cv2.createTrackbar("US", 'trackbars', 0, 255, nothing)
cv2.createTrackbar("UV", 'trackbars', 0, 255, nothing)

while True:
    ret, frame = cap.read()

    # getting trackbars positions
    lower_hue = cv2.getTrackbarPos("LH", "trackbars")
    lower_saturation = cv2.getTrackbarPos("LS", "trackbars")
    lower_value = cv2.getTrackbarPos("LV", "trackbars")
    upper_hue = cv2.getTrackbarPos("UH", "trackbars")
    upper_saturation = cv2.getTrackbarPos("US", "trackbars")
    upper_value = cv2.getTrackbarPos("UV", "trackbars")

    # masking image with hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
