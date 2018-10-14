# ARDrone
## Python Tutorial
1. Create .proto File
2. Create .py File
   - Establish A Connection With The Drone
   - Store & Encode Drone Sensor Data Through Protocol Buffer

[Google Protocol Buffer Documentation](https://developers.google.com/protocol-buffers/docs/pythontutorial)
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
## Compile Required pb2.py For Protocol Buffer
```bash
pip install protobuf
sudo apt install protobuf-compiler
protoc -I=. --python_out=. ./filename.proto
```
