import pymongo
from pymongo import MongoClient
import glob
import base64
import json
import cv2
client = MongoClient()
path = 'data (copy)/train1/hillary/*.jpg'  #  directory from which images were fetched
files = glob.glob(path)
# accessing the 'hillary' collection of the database 'images'
# similarly we need to do it for 'trump' and 'none' collection
db = client.images.hillary # change the collection here accordingly

# encoding and storing the data (images)

for name in files:
	with open(name,"rb") as img:
		encoded_string = base64.b64encode(img.read())
		db.insert({'image':encoded_string, 'class':'hillary'})
		
count=1

#############################################################
# the following code is to regenerate back the data from MongoDB #
#############################################################
"""
for obj in client.images.hillary.find():
	# print obj['class']
	img1 = base64.b64decode(obj['image'])
	with open('data (copy)/train1/new/' + str(count) +".jpg", "wb") as f:
		f.write(img1)
		count+=1 
"""
