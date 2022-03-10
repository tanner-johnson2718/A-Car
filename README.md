# A-Car
Repo to hold content for a nerf mounter RC Car. Will use a linux based x86
device to serve as car controller. Will have a wifi card and XBOX 360 ctlr to
on the x86 controller with a UI to drive/operation vehicle and display car 
sensors such as acceleromoters, speed, video feed from vehicle, current 
connection status, etc. The vehicle itself will be standard cheep RC car 
"hacked" to be a controlled by a beaglebone blue. Initial goal it to simply
get the vehicle moving and operational and mount a nerf gun later.

... given the base OS has a lot if functionality need to rework tasking...


# Control Tasks
- [X] Get XBOX controller working i.e. can detect controller input
- [X] Get vid cam input window
- [X] Talk directly between two wifi card, no router, maybe use BLE?
- [ ] Send Video and Controller Signal over WiFi direct (or BLE)
- [ ] UI for displaying connection and car status and signals

# MCU Task
- [X] Get beaglebone blue minimally running linux
- [X] Custom Linux to get right drivers?
- [X] Get IMU gyros and other on board sensors up
- [X] Get on board WiFi up
- [ ] Get vid cam streaming back to controller
- [ ] Control a DC motor with the board
- [ ] Control a servo with the board
- [ ] Control a rotary encoder with the board

# Vehicle Operation Tasks
- [ ] ... todo .. get board and RC car to interoperate

# Major Integration Tasks
- [ ] ... todo

# SW Deps
- Linux x86
    - dkms
    - xpad driver
    - vlc
- Linux for beagle bone
    - v4l
    - proper drivers

# Hardware
- x86 linux PC
- Beaglebone blue
- Spare DC motor for testing 
- Spare servo for testing
- Spare rotary encoder for testing
- Xbox controller
- USB web cam
