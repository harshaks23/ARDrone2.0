
import ardrone,numpy,cv2

drone = ardrone.ARDrone()
print(drone.image)

open_cv_image = numpy.array(drone.image) 
# Convert RGB to BGR 
open_cv_image = open_cv_image[:, :, ::-1].copy() 
print(open_cv_image)
