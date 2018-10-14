# USAGE
# python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

# import the necessary packages

import numpy as np
import argparse
import imutils
import time
import cv2,numpy
import parse_sensor_data 
import ardrone

from PIL import Image




# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect, then generate a set of bounding box colors for each class
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))


net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])


#frame=vs.read()
	
frame = parse_sensor_data.drone.image
frame.show()


open_cv_image =numpy.array(frame)
	
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
from clarifai.rest import Video as ClVideo
app = ClarifaiApp(api_key='4457471b3f58454d98334e08cad1e593')

model = app.models.get('general-v1.3')

#print("file_obj",file_obj)

a=model.predict([ClImage(frame)])

b=a["outputs"][0]["data"]["concepts"]
for i in b:
    print(i["name"])

frame =open_cv_image[:,:,::-1].copy()
frame = imutils.resize(frame, width=400)

# grab the frame dimensions and convert it to a blob
(h, w) = frame.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
		0.007843, (300, 300), 127.5)

# pass the blob through the network and obtain the detections and
	# predictions
net.setInput(blob)
detections = net.forward()

	# loop over the detections
for i in np.arange(0, detections.shape[2]):
		# extract the confidence (i.e., probability) associated with
		# the prediction
	confidence = detections[0, 0, i, 2]

		# filter out weak detections by ensuring the `confidence` is
		# greater than the minimum confidence
	print(confidence,"da",args["confidence"])
	if confidence > args["confidence"]:
		idx = int(detections[0, 0, i, 1])
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

			# draw the prediction on the frame
		label = "{}: {:.2f}%".format(CLASSES[idx],
				confidence * 100)
		print("label",label) 
		


parse_sensor_data.drone.halt()


