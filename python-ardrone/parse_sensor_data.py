from PIL import Image
from io import BytesIO
import time
import ardrone
import sensor_data_pb2

# Read In Data From ARDrone 2.0
def encodedata():
	sd = sensor_data_pb2.SensorData()

	sd.unix_time = drone.navdata['header']

	sd.battery = drone.navdata['demo']['battery']
	sd.altitude = drone.navdata['demo']['altitude']
	sd.pitch = drone.navdata['demo']['theta']
	sd.roll = drone.navdata['demo']['phi']
	sd.yaw = drone.navdata['demo']['psi']
	sd.vx = drone.navdata['demo']['vx']
	sd.vy = drone.navdata['demo']['vy']
	sd.vz = drone.navdata['demo']['vz']

	sd.fly = drone.navdata['state']['fly']

	image = sd.images.add()
	tempImage = drone.image
	image.width, image.height = tempImage.size
	image.image_data = tempImage.tobytes()

	# Encode Data Via Protocol Buffer
	encodedsd = sd.SerializeToString()
	#print(sensor_data_pb2.SensorData().FromString(encodedsd))
	#Image.frombytes('RGB', (image.width, image.height), image.image_data).show()
	return encodedsd

drone = ardrone.ARDrone()
time.sleep(0.125)

# Test
#for i in range(0,3):
#	encodedata()
#	time.sleep(1)
#drone.halt()
