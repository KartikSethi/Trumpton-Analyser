Trumpton Analyser is a facial recognition Web Application that analyses the given image and predict whether the image contains Hillary Clinton or Donald Trump or both or none of them.

### Link to the application: [Trumpton Analyser](http://kartik1295.pythonanywhere.com/)

### Different phases pertaining to this project

#### Data Collection:

* Collected the tweet data using both REST and Streaming APIs.
* Used REST API to retrieve data from Hillary Clinton's, Donald Trump's twitter handles and various news handles.
* Used Streaming API to retrieve data based on popular hashtags.
* All the python files used, create text files containing image URLs (present in the tweet) which can be used to download those images using 'wget -i <path>' command.


#### Face Detection:

* Used Haar-Cascades (present in OpenCV) to detect faces in the downloaded images.
* Detected faces were cropped out, resized to 64 X 64 dimensions and stored separately.
* Although the data set is pretty small but it is void of any noise (only negligible amount). One can check the data in 'Training Model/train1' directory.
* Stored the data in the MongoDB database named 'images' with collections name as 'hillary', 'trump' and 'none'.


#### Model Training:

* Trained three shallow convolutional neural network models (check Convnet.ipynb) on the above data. 
* Used Keras wrapper (with Theano backend) to construct the architecture of the model.
* Achieved moderate classification accuracy. Since the data used for training was very less, there are false positives present but the recall value is still pretty high.


#### Trumpton Application Approach:

* A user can upload an image pertaining to any of the three formats 'jpg', 'png' or 'bmp'.
* The uploaded image will be displayed along with one another image with all the faces detected (using Haar Cascades).
* All the faces present in the image (cropped out and resized to 64 X 64) will be fed into one of the models to predict their respective classes.('hillary' or 'trump' or 'none')
* Then took the intersection of all the predicted classes pertaining to each face of the image, to derive the output. 




