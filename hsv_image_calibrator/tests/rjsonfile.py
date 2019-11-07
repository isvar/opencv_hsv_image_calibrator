from pathlib import Path
import numpy as np
import cv2
import json

cap = cv2.VideoCapture(0)

hsv_data = Path("hsv_values.json").read_text()
hsv_values = json.loads(hsv_data)


while True:
    hsv_data = Path("hsv_values.json").read_text()
    hsv_values = json.loads(hsv_data)

    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color_values = np.array([hsv_values["lower_h"], hsv_values["lower_s"], hsv_values["lower_v"]])
    upper_color_values = np.array([hsv_values["upper_h"], hsv_values["upper_s"], hsv_values["upper_v"]])
    mask = cv2.inRange(hsv, lower_color_values, upper_color_values)

    cv2.imshow("mask", mask)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
