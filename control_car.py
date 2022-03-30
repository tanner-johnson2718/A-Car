from ctypes import sizeof
from operator import mod
import time

# import python socket library to host sensor server
import socket
import json

# init server
HOST = "192.168.8.1"
PORT = 8092
try:    # keep running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Control Service Connected by {addr}")
            while True:
                # Loop
                data = conn.recv(4)

                id = data[0]
                val = data[2] + (data[3] << 8)

                # signed short
                mod_val = val
                if (val >> 16) & 1:
                    mod_val = val - 2*(1<<16)
                
                
                print("ID="+str(id)+" VAL="+str(mod_val))
                    
except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nControl Service Exitting!")