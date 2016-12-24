"""
    Main app code
    Reference: https://github.com/ibininja/upload_file_python
"""

import os
import numpy as np
import cv2
from cv2 import *
import sys
import glob
import errno
import PIL
from PIL import Image
from keras.models import load_model
from os import listdir
from PIL import Image as PImage
from keras.preprocessing.image import ImageDataGenerator

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
model = load_model('model_with_more_pictures.h5')
model.load_weights('more_pictures.h5')
# model = load_model('model_without_cross_validation.h5')
# model.load_weights('weights_without_cross_validation.h5')
# model = load_model(model_cross_validation.h5')
# model.load_weights('weights_cross_validation.h5')
# model = load_model('gen_model.h5')
# model.load_weights('gen_model_weights.h5')

from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
count=1



def loadImages(path,imagesList):
   
    loadedImages = []
    for image in imagesList:
        img1 = PImage.open(path +'/'+ image)
        img = img1.copy()
        img1.close()
        loadedImages.append(img)
    return loadedImages

@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))
    global count
    flag = 0
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        # This is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp"):
            print("File supported moving on...")
        else: 
            print "file not supported"
            flag = 1
            return render_template("error.html")
            # break
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        name = target + '/' + str(upload.filename)

    
    if (not flag):
        img = cv2.imread(name)
        hillary = False
        trump = False
        imageList = []
        X_test = []
        path = ""
        flag2 = 0
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.028, 5)
        current_count = count

        for (x, y, w, h) in faces:
            flag2 = 1
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            img1 = cv2.resize(roi_color, (64,64), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
            edited_name = str(count) + '_' + filename
            path = 'edited'
            imageList.append(edited_name)
            cv2.imwrite('edited/' + str(count) + '_' + filename , img1)
            count+=1
        
        if flag2:
            imgs = loadImages(path,imageList)
            for image in imgs:
                X_test.append(np.asarray(image))
            for i in xrange(len(X_test)):
                X_test[i] = np.swapaxes(X_test[i], 2, 0)
            X_test = np.array(X_test)
            Y_predict = model.predict(X_test, batch_size=1, verbose=0)
            for score in Y_predict:
                index = np.argmax(score)
                print index
                if index == 0:
                    if (abs(score[1] - score[0]) < 0.1):
                        hillary = True
                    elif (abs(score[2]- score[0]) < 0.1):
                        trump = False
                    else:
                        trump = True
                elif index == 1:
                    if (abs(score[0] - score[1]) < 0.1):
                        trump = True
                    elif (abs(score[2]- score[1]) < 0.1):
                        hillary = False
                    else:
                        hillary = True
                else:
                    if (abs(score[0] - score[2]) < 0.1):
                        trump = True
                    elif (abs(score[1] - score[2]) < 0.1):
                        hillary = True



        
        detected = 'detected_' + str(current_count) + '_' + filename
        cv2.imwrite('images/detected_' + str(current_count) + '_' + filename, img)
        # prediction of classes
        return render_template("complete.html", image_name=filename, detected=detected, trump=trump,hillary=hillary)


@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)




if __name__ == "__main__":
    app.run(debug=True)
