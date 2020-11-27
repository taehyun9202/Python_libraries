import cv2
import numpy as np


image = np.full((512, 512, 3), 0, np.uint8)
line = cv2.line(image.copy(), (0, 0), (255, 255), (255, 0, 0), 5)

cv2.imshow('line', line)
cv2.waitKey(0)

rec = cv2.rectangle(image.copy(), (20, 20), (255, 255), (0, 0, 255), -1)

cv2.imshow('rec', rec)
cv2.waitKey(0)

cir = cv2.circle(image.copy(), (255, 255), 50, (0, 255, 0), -1)
cv2.imshow('cir', cir)
cv2.waitKey(0)

points = np.array([[0, 0], [255, 200], [512, 0], [310, 255], [512, 512], [255, 310], [0, 512], [200, 255]])
poly = cv2.polylines(image.copy(), [points], True, (255, 255, 255), 2)
cv2.imshow('poly', poly)
cv2.waitKey(0)

text = cv2.putText(image.copy(), "Hello World", (90, 255), cv2.FONT_ITALIC, 2, (255, 255, 255), 5) # text, location, font, size, color, bold
cv2.imshow('text', text)
cv2.waitKey(0)