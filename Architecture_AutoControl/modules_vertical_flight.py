from io import BytesIO
import sensor_data_pb2

def vertical_flight(input):
	data = ''

	encodedsd = input['sensors']
	decodedsd = sensor_data_pb2.SensorData().FromString(encodedsd)

	# Change Directions If Drone Is Too High Or Too Low
	if(decodedsd.fly == 0):
		print("TakeOff Scheduled")
		return {
		    'has_command': True,
		    'meta_id': 'takeoff',
		    'data': data,
	    }
	else:
		if(decodedsd.altitude < 900):
			print("UP"),
			print(decodedsd.altitude)
			return {
			    'has_command': True,
			    'meta_id': 'up',
			    'data': data,
		    }
		elif(decodedsd.altitude > 1500):
			print("DOWN"),
			print(decodedsd.altitude)
			return {
			    'has_command': True,
			    'meta_id': 'down',
			    'data': data,
		    }
		else:
			return {
			    'has_command': True,
			    'meta_id': 'nothing',
			    'data': data,
		    }