# Python script to create dummy stream to PC side client. Sends fake gyro,
# accel and magnometer to client to test client functionality

# import python socket library to host sensor server
import socket
import json
import numpy as np
import time

# init server
HOST = "127.0.0.1"
PORT = 8091

try:    # keep running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            
            print("Sensor Service Connected by " + str(addr))
            counter = 0

            while True:

                # Generate dummy data
                a = [1, np.cos(counter), np.sin(counter)]
                g = [np.cos(counter), 1, np.sin(counter)]
                m = [np.cos(counter), np.sin(counter), 1]
                data = {}
                data['accel'] = a
                data['gyro']  = g
                data['mag']   = m

                conn.sendall(json.dumps(data).encode())
                time.sleep(.5)  # sleep some
                counter += 1
                    
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\Sensor Service Exitting!")