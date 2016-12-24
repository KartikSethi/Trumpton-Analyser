""" 
	File to detect faces in images, using haarcascades (present in opencv-2).
	Detected faces are cropped out, resized (into a 64 X 64 image) and saved
	as different files.
	Reference: http://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html
""" 

import numpy as np
import cv2 # open cv import
import sys
import glob
import errno
import PIL
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')


gcount = 1
path = 'hash/test/*.jpg'
# path = <path/*.jpg>, # add the path here from which you want to extract the files
files = glob.glob(path)


for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
	lcount = 1
	flag = 0
	img = cv2.imread(name)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.028, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		if flag == 0:
		    path = "hash/hash_" + str(gcount) + ".jpg" # name accordinly
		    flag = 1
		elif flag == 1:
		    path = "hash/hash_" + str(gcount) + "_" + str(lcount) + ".jpg"
		    lcount += 1
		img1 = cv2.resize(roi_color,(64,64),fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
		cv2.imwrite(path, img1)
	gcount += 1
		

		