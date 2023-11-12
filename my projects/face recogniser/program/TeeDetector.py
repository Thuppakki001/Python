import cv2
import os
cap = cv2.VideoCapture(0)
dir = r'C:\Users\tarun\OneDrive\Documents\learning\Programming\python\my projects\machine learning\training\tee'
while True:
    _, img = cap.read()
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == 27:
        break
