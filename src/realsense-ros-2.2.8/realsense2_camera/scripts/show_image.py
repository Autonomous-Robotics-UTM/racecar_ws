import numpy as np
import cv2
import os

# Load an color image in grayscale
img = cv2.imread('robot.jpg',0)

cv2.imshow('image',img)
cv2.waitKey(0)
path = '/home/michael/'
path = os.getenv("HOME") + "/Pictures"
cv2.imwrite(os.path.join(path , 'gray.png'),img)
cv2.destroyAllWindows()
