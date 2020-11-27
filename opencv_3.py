import cv2
import numpy as np

image = cv2.imread('image.jpg')

# cv2.imshow('image', image)
# cv2.waitKey(0)
#
# expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('expand', expand)
# cv2.waitKey(0)
#
#
# shrink = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
# cv2.imshow('expand', shrink)
# cv2.waitKey(0)

height, width = image.shape[:2]

# M = np.float32([[1, 0, 200], [0, 1, 100]])
# dst1 = cv2.warpAffine(image, M, (width, height))
# cv2.imshow('shift', dst1)
# cv2.waitKey(0)

M = cv2.getRotationMatrix2D((width / 2, height / 2), 90, .6)
dst2 = cv2.warpAffine(image, M, (width, height))
cv2.imshow('rotate', dst2)
cv2.waitKey(0)

