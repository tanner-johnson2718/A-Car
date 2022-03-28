# A-Car
Repo to hold content for a nerf mounter RC Car. Will use a linux based x86
device to serve as car controller. Will have a wifi card and XBOX 360 ctlr to
on the x86 controller with a UI to drive/operation vehicle and display car 
sensors such as acceleromoters, speed, video feed from vehicle, current 
connection status, etc. The vehicle itself will be standard cheep RC car 
"hacked" to be a controlled by a beaglebone blue. Initial goal it to simply
get the vehicle moving and operational and mount a nerf gun later.

# Network
The network than connects the board to the PC will be hosted via wifi end point
on the board. The network ESSID is "BeagleBone-9947" with password "BeagleBone".
The board itself will host several services that allow one to control and 
interface with the device such as ssh, the cloud 9 IDE and debugger, and also

| Decription  |  IP | Port  | Notes |
| --- | ---  | -------- | ---------- |
| SSH Host | 192.168.8.1 | 22 | User is debian and password is temppwd |
| Control Interface | 192.168.8.1 | 8090 | Car Control Interface |

# Initial Proof of Concept Tasking
- [X] Get XBOX controller working i.e. can detect controller input
- [X] Get BBB up with linux, proper drivers, and on same network as PC
- [X] Stream web cam video form BBB to PC
- [X] Get IMU gyros and other on board sensors up
- [ ] Control a DC motor with the board
- [ ] Control a servo with the board
- [ ] Control a rotary encoder with the board

# Control Interface
- [ ] Fork and modify mjpg-streamer so only web cam is displayed
- [ ] Also display on board imu sensor data on hosted web page
- [ ] Send controller inputs to board and display on web page
- [ ] Some extra data to be displayed eventually: signal strength, dropped
      packets, battery life and discharge, power consuption, ... definetly more
      can be added here.

# Vehicle Operation and Integration Tasks
- [ ] ... todo .. get board and RC car to interoperate

# SW Deps
- Linux x86
    - dkms
    - xpad driver
    - vlc
    - ffmpeg
- Linux for beagle bone
    - v4l
    - ffmpeg
    - cmake
    - gcc
    - g++
    - libjpeg8-dev
    - mjpg-streamer

# Hardware
- x86 linux PC
- Beaglebone blue (BBB)
- Spare DC motor for testing 
- Spare servo for testing
- Spare rotary encoder for testing
- Xbox controller
- USB web cam
- 12V power supply for BBB