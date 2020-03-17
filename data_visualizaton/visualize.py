import cv2 as cv
import os
from os.path import expanduser
home = expanduser("~")

images_path = home + '/image_data/images/'
labels_path = home + '/image_data/labels.txt'
lineThickness = 10
img_heigth = 480
img_width = 640

# in ms
speed = 600 

im_files = [f for f in os.listdir(images_path)]

# get time stamps
labels = {}
with open(labels_path, 'r') as lf:
	for line in lf:
		stamp, angle = line.strip('\n').split(' ')
		labels[stamp] = angle

#print(labels)

for f in im_files:
	im = cv.imread(images_path + f)

	stamp = f.strip('.jpg')
	print(labels[stamp])
	angle = int(float(labels[stamp]) * 100)
	cv.line(im, (img_width/2, img_heigth/2), (img_width/2 + angle, img_heigth/2), (0,255,0), lineThickness)
	cv.line(im, (img_width/2 + angle, img_heigth/2 - 4), (img_width/2 + angle, img_heigth/2 + 8) , (0,255,0), lineThickness)

	cv.imshow('display', im)

	cur_speed = speed
	if angle == 0:
		cur_speed /= 3	

	cv.waitKey(cur_speed)

waitKey()
