#!/usr/bin/env python3
# Read and display IMU
# Based on: https://raw.githubusercontent.com/mcdeoliveira/rcpy/master/examples/rcpy_test_imu.py
# import python libraries
from ctypes import sizeof
import time
import getopt, sys

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.mpu9250 as mpu9250

# import python socket library to host sensor server
import socket
import json

# init imu
rcpy.set_state(rcpy.RUNNING)
mpu9250.initialize(enable_magnetometer = True)

# init server
HOST = "192.168.8.1"
PORT = 8091
try:    # keep running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print("Sensor Service Connected by " + str(addr))
            while True:
                if rcpy.get_state() == rcpy.RUNNING:
                    temp = mpu9250.read_imu_temp()
                    data = mpu9250.read()
                    conn.sendall(json.dumps(data).encode())
                    time.sleep(.25)  # sleep some
                    
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\Sensor Service Exitting!")