import cv2
import numpy as np

image = cv2.imread('digit.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)

print(x.shape)

train = x[:, :].reshape(-1, 400).astype(np.float32)
print(train.shape)

k = np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]

np.savez('trained.npz', train=train, train_labels=train_labels)
