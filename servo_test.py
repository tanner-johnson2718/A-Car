#!/usr/bin/env python3
# import python libraries
import time, math
import getopt, sys

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.servo as servo
import rcpy.clock as clock

# defaults
duty = 1.5
period = 0.02
channel = 8

# set state to rcpy.RUNNING
rcpy.set_state(rcpy.RUNNING)

# set servo duty (only one option at a time)
srvo = servo.Servo(channel)
srvo.set(duty)
clck = clock.Clock(srvo, period)
    
try:
    servo.enable()
    clck.start()

    while True:
        time.sleep(1)
            
except KeyboardInterrupt:
    # handle what to do when Ctrl-C was pressed
    pass
        
finally:

    # stop clock
    clck.stop()
    # disable servos
    servo.disable()
    # say bye
    print("\nBye Beaglebone!")