import cv2
import numpy as np
import time

def nothing():
    pass


cap = cv2.VideoCapture(0)


while not cap.isOpened():
    print("No se ha encontrado la camara")
    time.sleep(1.0)
else:
    print("conectado")


cv2.namedWindow("trackbars")

# trackbars creation
cv2.createTrackbar("LH", 'trackbars', 0, 180, nothing)
cv2.createTrackbar("LS", 'trackbars', 0, 255, nothing)
cv2.createTrackbar("LV", 'trackbars', 0, 255, nothing)
cv2.createTrackbar("UH", 'trackbars', 180, 180, nothing)
cv2.createTrackbar("US", 'trackbars', 255, 255, nothing)
cv2.createTrackbar("UV", 'trackbars', 255, 255, nothing)

while True:
    ret, frame = cap.read()

    # getting trackbars positions
    lower_hue = cv2.getTrackbarPos("LH", "trackbars")
    lower_saturation = cv2.getTrackbarPos("LS", "trackbars")
    lower_value = cv2.getTrackbarPos("LV", "trackbars")
    upper_hue = cv2.getTrackbarPos("UH", "trackbars")
    upper_saturation = cv2.getTrackbarPos("US", "trackbars")
    upper_value = cv2.getTrackbarPos("UV", "trackbars")

    # masking image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([lower_hue, lower_saturation, lower_value])
    upper_blue = np.array([upper_hue, upper_saturation, upper_value])
    blur = cv2.GaussianBlur(hsv, (5, 5), 0)
    erode = cv2.erode(blur, (5,5))
    mask = cv2.inRange(erode, lower_blue, upper_blue)

    cv2.imshow("frame", frame)
    # cv2.imshow("blur", blur)
    cv2.imshow("mask", mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
