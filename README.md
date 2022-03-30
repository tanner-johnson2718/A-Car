# A-Car
Repo to hold content for a nerf mounter RC Car. Will use a linux based x86
device to serve as car controller. Will have a wifi card and XBOX 360 ctlr to
on the x86 pc with a UI to drive/operation vehicle and display car 
sensors such as acceleromoters, speed, video feed from vehicle, current 
connection status, etc. The vehicle itself will be standard cheep RC car 
"hacked" to be a controlled by a beaglebone blue. Initial goal it to simply
get the vehicle moving and operational and mount a nerf gun later.

# Network
The network than connects the board to the PC will be hosted via wifi end point
on the board. The network ESSID is "BeagleBone-9947" with password "BeagleBone".
The board itself will host several services that allow one to control and 
interface with the device such as ssh, the cloud 9 IDE and debugger, and also
video stream and control interface services to see camera output and push 
controller input to board.

| Decription  |  IP | Port  | Notes | Vehicle Host Process | PC Client Process |
| --- | ---  | -------- | ---------- | --- | --- |
| SSH Host | 192.168.8.1 | 22 | User is debian and password is temppwd | Open SSH linux host service | Open SSH client command |
| Video Interface | 192.168.8.1 | 8090 | Video Stream Interface | mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -p 8090 -w /usr/local/share/mjpg-streamer/www" | firefox http://192.168.8.1:8090/ctlr.html |
| Sensor Stream | 192.168.8.1 | 8091 | Stream to send sensor data | sensor_car.py | sensor_pc.py |
| Control Stream | 192.168.8.1 | 8092 | Stream to send controller input | control_car.py | ctlr |
| Cloud 9 debugger | 192.168.8.1 | 80 | Address of 192.168.8.1 resolves to debugger hosted on board | ?? | firfox 192.168.8.1 |

# Initial Proof of Concept and Bring Up Tasking
- [X] Get XBOX controller working i.e. can detect controller input
- [X] Get BBB up with linux, proper drivers, and on same network as PC
- [X] Get IMU gyros and other on board sensors up
- [ ] Control a DC motor with the board
- [ ] Use osciliscope to snoop DC motor curciut
- [ ] Control a servo with the board
- [ ] Use osciliscope to snoop servo curciut

# Control Interface
- [X] Stream web cam video form BBB to PC
- [X] Fork and modify mjpg-streamer so only web cam is displayed
- [X] Also display on board imu sensor data
- [ ] Send controller inputs to board and display on web page

# Vehicle Operation and Integration with Control Interface
- [ ] ... todo .. get board and RC car to interoperate

# Build and Design Independant Turret
- [ ] ...

# Mount and Integrate Turret with Vehicle
- [ ] ...

# SW Deps
- Linux x86
    - dkms
    - xpad driver
    - vlc
    - ffmpeg
    - gcc
    - python3
- Linux for beagle bone
    - v4l
    - ffmpeg
    - cmake
    - gcc
    - g++
    - libjpeg8-dev
    - mjpg-streamer
    - python3

# Hardware
- x86 linux PC
- Beaglebone blue (BBB)
- Spare DC motor for testing 
- Spare servo for testing
- Spare rotary encoder for testing
- Xbox controller
- USB web cam
- 12V power supply for BBB