import cv2

cap = cv2.VideoCapture(0)
while True:
    _, img = cap.read()
    cv2.imshow("img", img)
    key = cv2.waitKey(1)
    if key == 27:
        break
