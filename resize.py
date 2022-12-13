# Import necessary modules
import cv2
import os

img = cv2.imread('data/background.png')
frame = cv2.resize(img,(960,540))
cv2.imwrite(os.path.join("data", 'back.png'), frame)