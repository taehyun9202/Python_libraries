import cv2
import time

image = cv2.imread('image.jpg')
# print(image.shape)
# print(image.size)
#
# px = image[100, 100]  # bgr
# print(px)
# print(px[2])

# start_time = time.time()
# for i in range(0, 101):
#     for j in range(0, 101):
#         image[i, j] = [255, 255, 255]
# print("----- %s seconds -----" % (time.time() - start_time))
#
# img1 = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# cv2.imshow('white', img1)
# cv2.waitKey(0)
#
# start_time = time.time()
# image[0:100, 0:100] = [0, 0, 0]
# print("----- %s seconds -----" % (time.time() - start_time))
#
# img2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('black', img2)
# cv2.waitKey(0)


# roi = image[100:500, 500:950]
# cv2.imshow('ROI', roi)
# cv2.waitKey(0)
#
# image[0:400, 0:450] = roi
# cv2.imshow('ROI added', image)
# cv2.waitKey(0)

image[:, :, 2] = 0
cv2.imshow('No red', image)
cv2.waitKey(0)

image[:, :, 1] = 0
cv2.imshow('No green', image)
cv2.waitKey(0)

image[:, :, 0] = 0
cv2.imshow('No blue', image)
cv2.waitKey(0)


