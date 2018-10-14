# ARDrone
## Setup Environment
```bash
sudo apt install python-pip
sudo apt install python-dev
sudo apt install libavcodec-dev
sudo apt install libavformat-dev
sudo apt install libswscale-dev

pip install image
pip install ardrone
```
## Commands
```python
# Shutdown Drone Communication (Run At End Of Session)
.halt()

# Hover
.hover()

# Land
.land()

# Move (i -> Left-Right Tile, j -> Front Back Tilt, K -> Vertical Speed, L -> Angular Speed)
.move(i, j, k, l)

# Move ___
.move_foo()
    left
    right
    up
    down
    forward
    backward

# Set Camera (0 -> Front Camera, 1-> Bottom Camera)
.set_cam(i)

# Set Speed
.set_speed(i)

# Take Off
.takeoff()

# Trim/Calibrate
.trim()

# Turn___
.turn_foo()
    left
    right
```
# Measurement Readings
```python
# Image (PIL.Image)
.image

# Navigation Data
.navdata['foo']
    'header'

.navdata['demo']['foo`]
    'battery'
    'altitude'
    'theta'
    'phi'
    'psi'
    'vx'
    'vy'
    'vz'

.navdata['state']['foo']
    'fly'
```