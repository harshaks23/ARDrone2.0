# USAGE: python real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel

import numpy as np
import argparse
import imutils
import time
import cv2,numpy
import parse_sensor_data 
import ardrone
import sensor_data_pb2
from PIL import Image

min_confidence = 0.25

def vision(img):
	# List Storage For Labels
	list_=[]

	# Min Confidence Level For Detections
	global min_confidence
	
	# Initialize The List Of Class Labels MobileNet SSD Was Trained To Detect & Generate Bounding Box Color For Each Class
	CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
		"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
		"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
		"sofa", "train", "tvmonitor"]
	COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

	# Paths
	net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')

	# Image & OpenCV Image
	frame = parse_sensor_data.drone.image
	open_cv_image = numpy.array(frame)

	# Resize
	frame = open_cv_image[:,:,::-1].copy()
	frame = imutils.resize(frame, width=400)

	# Grab Frame Dimensions & Convert It To Blob
	(h, w) = frame.shape[:2]
	blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
			0.007843, (300, 300), 127.5)

	# Pass The Blob Through The Network & Obtain Detections
	net.setInput(blob)
	detections = net.forward()

	# Loop Over Detections
	for i in np.arange(0, detections.shape[2]):
		confidence = detections[0, 0, i, 2]
		if confidence > min_confidence:
			idx = int(detections[0, 0, i, 1])
			box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
			(startX, startY, endX, endY) = box.astype("int")

			label = "{}: {:.2f}%".format(CLASSES[idx],
					confidence * 100)
			list_.append(label)

	# Return List Storage
	return list_

def image_recognition(input):
	data = ''
	# Convert Encoded Input To Image
	encodedsd = input['sensors']
	decodedsd = sensor_data_pb2.SensorData().FromString(encodedsd)

	img = Image.frombytes('RGB', (decodedsd.images[0].width, decodedsd.images[0].height), decodedsd.images[0].image_data)

	# Compile Valid Objects Detected List
	temp_objects = vision(img)
	valid_objects = []
	for i in temp_objects:
		if(float(i.split(":")[1].strip(' \t\n\r%')) > min_confidence):
			valid_objects.append(i.split(":")[0])

	valid_objects = list(set(valid_objects))
	print("Valid Objects: ", valid_objects)

	# Search For Desired Object
	if("bottle" in valid_objects):
		print("Bottle")
		if decodedsd.fly == 0:
			return {
	   		    'has_command': True,  
	        	'meta_id': 'takeoff',
	    		'data': data,
	    	}
		else:
			return {
	   		    'has_command': True,  
	        	'meta_id': 'hover',
	    		'data': data,
	    	}
	elif("person" in valid_objects):
		print("Person")
		if decodedsd.fly == 0:
			return {
				'has_command': True,  
				'meta_id': 'takeoff',
				'data': data,
			}
		else:
			return {
				'has_command': True,  
				'meta_id': 'spin',
				'data': data,
			}
	else:
		return {
			'has_command': False,
		}