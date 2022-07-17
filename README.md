# A-Car
First iteration of RC car project. The RC car project will be a 3D printed,
custom built RC car controlled by a laptop with an XBOX controller connected
to it. This first iteration will have the following features and milestones.

- Use out of box OS and SW for Beagle Bone Blue (On-Vehicle controller).
- Board bring up and initial testing.
- Build and Print RC car using 3D printer and standard DC motor and servos
- Send and display sensor and camera data from vehicle on controlling laptop
- Control car with XBOX controller
- Gather and display imporant vehicle performance metrics (See below)

# Network, Processes and Services
The network that connects the board to the PC will be hosted via wifi end point
on the board. The network ESSID is "BeagleBone-9947" with password "BeagleBone".
The board itself will host several services that allow one to control and 
interface with the device such as ssh, the cloud 9 IDE and debugger, and also
video stream and control interface services to see camera output and push 
controller input to board.

| Decription  |  IP | Port  | Notes | Vehicle Host Process | PC Client Process |
| --- | ---  | -------- | ---------- | --- | --- |
| SSH Host | 192.168.8.1 | 22 | User is debian and password is temppwd | Open SSH linux host service | Open SSH client command |
| Video Interface | 192.168.8.1 | 8090 | Video Stream Interface | mjpg_streamer -i "input_uvc.so -d /dev/video0" -o "output_http.so -p 8090 -w /usr/local/share/mjpg-streamer/www" | firefox http://192.168.8.1:8090/ctlr.html |*/
| Sensor Stream | 192.168.8.1 | 8091 | Stream to send sensor data | sensor_car.py | sensor_pc.py |
| Control Stream | 192.168.8.1 | 8092 | Stream to send controller input and control vehicle | control_car.py | ctlr |
| Cloud 9 debugger | 192.168.8.1 | 80 | Address of 192.168.8.1 resolves to debugger hosted on board | ?? | firefox 192.168.8.1 |

## SW Dep
- Linux x86 (Ubuntu 20.04)
    - dkms
    - xpad driver
    - gcc
    - python3
    - firefox (web browser)
- Linux for beagle bone (Debian 10.3)
    - v4l
    - cmake
    - gcc
    - g++
    - libjpeg8-dev
    - python3
    - rcpy / librobotcontrol

# Initial Proof of Concept and Bring Up Tasking
- [X] Get XBOX controller working i.e. can detect controller input
- [X] Get BBB up with linux, proper drivers, and on same network as PC
- [X] Get IMU gyros and other on board sensors up
- [X] Control a DC motor with the board
- [X] Use osciliscope to snoop DC motor curciut
- [X] Control a servo with the board
- [X] Use osciliscope to snoop servo curciut
- [X] Test with battery

# Control Interface / Software Tasks
- [X] Stream web cam video form BBB to PC
- [X] Fork and modify mjpg-streamer so only web cam is displayed
- [X] Also display on board imu sensor data
- [X] Send controller inputs to board and display on web page
- [X] Display sensor data using matplotlib

# Vehicle Desgin, Contruction, and Testing

- [X] Solder quick connects to DC motor controler on board
- [X] Design wheels to mount directly to DC motors
- [X] Design motor housing
- [X] Design suspension
- [X] Design Frame
- [ ] Print, refine tolerances and assemble
- [ ] Write code to control vehicle
- [ ] Write code for gathering performance metrics

## Vehicle Performance Testing

| Metric | Description | Units |
| --- | --- | --- |
| Acceleration | Acceleration curve | m/s^2 |
| Velocity | Max speed | m/s |
| Vibration | Average length of gyro vector | deg / s |
| Power Consumption Curve | How much power drawn at given load | W |
| Signal integerity Curve | How much range can I go without lossing Coms | m |

# Materials

| Material | Qty | Description |
| --- | --- | --- |
| x86 linux PC | 1 | Ubuntu 20.04 HP Desktop |
| Beaglebone blue (BBB) | 1 | Rev A2 |
| Xbox 360 controller | 1 | W/ USB adapter |
| USB web cam | 1 | Logitech CV 270 |
| 12V power supply for testing BBB | 1 | 2A, barrel connector |
| CR-18 55T DC Motors | 2 | need data sheet |
| HS-422 servos | 2 | need data sheet |
| M4 Nuts and Bolts | 20+ | 4mm diameter, various length |
| PLA 1.75mm 3D printer filament | 1Kg | ? |
| LiPo Battery | 1 | Hobby Plus 600 mAh, 7.4V 2 cell |

# SW Development Workflow

# Conclusion and Next Steps

# Pictures and Videos of Final Product