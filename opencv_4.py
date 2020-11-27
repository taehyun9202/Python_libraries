import cv2

image1 = cv2.imread('image.jpg')
image2 = cv2.imread('image2.jpg')


result = cv2.add(image1, image2)
cv2.imshow('ius', result)
cv2.waitKey(0)

result2 = image1 + image2
cv2.imshow('ius', result2)
cv2.waitKey(0)