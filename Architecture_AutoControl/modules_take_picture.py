import sensor_data_pb2
import time

next_time = 0
interval = 5

def take_picture(input):
	meta_id = 'take_pic'
	data = ''

	# Global Variables
	global next_time
	global interval

	# If Timer
	cur_time = time.time()
	if cur_time > next_time:
		encodedsd = input['sensors']
		decodedsd = sensor_data_pb2.SensorData().FromString(encodedsd)

		# Get Image Constraints
		#Image.frombytes('RGB', (decodedsd.images[0].width, decodedsd.images[0].height), decodedsd.images[0].image_data).show()
		print("Picture Scheduled")
		data = {
			'width': decodedsd.images[0].width,
			'height': decodedsd.images[0].height,
			'bytes': decodedsd.images[0].image_data,
		}

		# Update next_time
		next_time = cur_time + interval

		return {
			'has_command': True,  
			'meta_id': meta_id,
			'data': data,
		}
	# Else
	else:
		return {
			'has_command': False,
		}